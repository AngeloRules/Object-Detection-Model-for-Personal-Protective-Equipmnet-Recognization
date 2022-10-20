from bing_image_downloader import downloader

downloader.download(
        query='People without protective equipment',
        limit=100,
        output_dir='downloads',
        adult_filter_off=True,
        force_replace=False,
        verbose=True,
        timeout=15,
        filter=['clipart','gif','transparent','line'])

    