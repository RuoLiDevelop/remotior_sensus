from unittest import TestCase

import remotior_sensus
from remotior_sensus.util import files_directories


class TestDownloadProducts(TestCase):

    def test_download_products(self):
        rs = remotior_sensus.Session(
            n_processes=2, available_ram=1000, log_level=10
        )
        cfg = rs.configurations
        cfg.logger.log.debug('test')
        cfg.logger.log.debug('>>> test query database Sentinel-2')

        tile_name = '33TTG'
        start_period_date = '2022-07-01'
        end_period_date = '2022-07-30'
        maximum_cloud_cover = 10
        # query the database
        query_result = rs.download_products.search(
            product='Sentinel-2', date_from=start_period_date,
            date_to=end_period_date, max_cloud_cover=maximum_cloud_cover,
            name_filter=tile_name
        )
        product_table = query_result.extra['product_table']
        print('product_table', product_table)
        filtered_table = product_table
        downloaded_images = rs.download_products.download(
            product_table=filtered_table,
            band_list=['04', '08'],
            output_path=cfg.temp.dir + '/downloaded_images',
        )

        """
        coordinate_list = [8, 43, 10, 41]
        output_manager = rs.download_products.query_sentinel_2_database(
            date_from='2020-01-01', date_to='2020-01-30', max_cloud_cover=80,
            result_number=5, coordinate_list=coordinate_list,
            name_filter='L2A'
        )
        product_table = output_manager.extra['product_table']
        self.assertEqual(product_table['product'][0], cfg.sentinel2)
        cfg.logger.log.debug('>>> test search')
        output_manager = rs.download_products.search(
            product=cfg.sentinel2, date_from='2020-01-01',
            date_to='2020-01-30', max_cloud_cover=80,
            result_number=5, coordinate_list=coordinate_list,
            name_filter='L2A'
        )
        product_table = output_manager.extra['product_table']
        self.assertEqual(product_table['product'][0], cfg.sentinel2)
        output_manager = rs.download_products.query_sentinel_2_database(
            date_from='2021-01-01', date_to='2021-01-10', max_cloud_cover=80,
            result_number=5, name_filter='33SVB'
        )
        product_table = output_manager.extra['product_table']
        self.assertEqual(product_table['product'][0], cfg.sentinel2)
        # export download links Sentinel-2
        cfg.logger.log.debug('>>> test export download links Sentinel-2')
        output_manager = rs.download_products.download(
            product_table=product_table, output_path=cfg.temp.dir,
            exporter=True
            )
        self.assertTrue(files_directories.is_file(output_manager.path))
        # download Sentinel-2 bands
        cfg.logger.log.debug('>>> test download Sentinel-2 bands')
        output_manager = rs.download_products.download(
            product_table=product_table[product_table['cloud_cover'] < 10],
            output_path=cfg.temp.dir + '/test_1', band_list=['01']
            )
        self.assertTrue(files_directories.is_file(output_manager.paths[0]))
        # download Sentinel-2 virtual bands
        cfg.logger.log.debug('>>> test download sentinel-2 virtual bands')
        output_manager = rs.download_products.download(
            product_table=product_table[product_table['cloud_cover'] < 10],
            output_path=cfg.temp.dir + '/test_2', band_list=['01'],
            virtual_download=True
            )
        self.assertTrue(files_directories.is_file(output_manager.paths[0]))
        # download Sentinel-2 virtual bands with subset
        cfg.logger.log.debug(
            '>>> test download sentinel-2 virtual bands with subset'
            )
        output_manager = rs.download_products.download(
            product_table=product_table[product_table['cloud_cover'] < 10],
            output_path=cfg.temp.dir + '/test_3', band_list=['01'],
            virtual_download=True,
            extent_coordinate_list=[494000, 4175000, 501000, 4169000]
            )
        self.assertTrue(files_directories.is_file(output_manager.paths[0]))
        cfg.logger.log.debug('>>> test query Sentinel HLS')
        output_manager = rs.download_products.query_nasa_cmr(
            product=cfg.sentinel2_hls, date_from='2021-01-01',
            date_to='2021-01-30', max_cloud_cover=80,
            result_number=20, coordinate_list=[11, 43, 12, 42]
        )
        product_table_2 = output_manager.extra['product_table']
        self.assertEqual(product_table_2['product'][0], cfg.sentinel2_hls)
        # export download links HLS
        cfg.logger.log.debug('>>> test export download links HLS')
        output_manager = rs.download_products.download(
            product_table=product_table_2, output_path=cfg.temp.dir,
            exporter=True
            )
        self.assertTrue(files_directories.is_file(output_manager.path))
        """

        ''' user and password required
        # download HLS bands
        cfg.logger.log.debug('>>> test download HLS bands')
        output_manager = download_products.download_sentinel2_images(
            product_table=product_table_2[product_table_2['cloud_cover'] < 10],
            output_path=cfg.temp.dir + '/test_4', band_list=['01'], 
            user='', password='')
        self.assertTrue(files_directories.is_file(output_manager.paths[0]))
        '''

        # clear temporary directory
        rs.close()
