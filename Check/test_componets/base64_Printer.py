import base64
import matplotlib.pyplot as plt
import io
from PIL import Image

# # jQuery1392123587184565609321_1562813099404({"key1":"iVBORw0KGgoAAAANSUhEUgAAAFoAAAAjCAIAAACb54pcAAAMmUlEQVR42s1aCViM2xufmhltRvumUbpJIiqJbmiTaBGplBYt1m4kRF1lGaSiLqGoexGX4h9ZkvV2LV0uyRUiW6lk2ktaRpvub/qmaShR6vo/z/t8z/ud75zznfM77/t73/ebIeUwC3sqL5mvHxe9vFecdaskI7U0LaXsysmy5AuxMfsrDkdVxkZU7Qp+G7aumrH63c9La3wX1i5xrXO3q3Owqp9pypo26b3BuIbxGo1jhjUNV2im8zfzCzWS+ZvJ5FaKyIeBki1S9OYhw5pURzWORjd0NmWZYSCGu9S5YSpM6PcuIKh6I14RXhW5pzJGIXHw0fL/nSg7i2VgMTdL7mJhWB4W2YutkT73YMHul7xSnx31SUuX8veV0V/TjStmybHY/DNm3nNm3sOip3eK718v+ftS6dUzZeePlycdqoiPqTwQWRUV9jaC8TY4oDpoxTs/r5ql7rXzHeucbeptp7MsjN6b6DXoazeOHdGoPrRJWa5ZXqxFjNIkyPeB3KOVEEL6IhD9LUPyDPXSArlvD7VbURt3qBcH2yeLJ3U/UTX9TOdG17B7kL6Cw/73K4IscSOXpcTtd0HhIzg6twrpe1dEKX5uDE1qyESHTWcZ1t1PLXv2BaGI045133P0PwuGP7b/pLHLbbOerO5XQyZ95aQzVhyHELqRW8RQTTPP6GwNYw/L5fFf/7JlJyK7bHeLeSBcKzPzeNJ/7Ke9h2PupjRhURlCdwlJF5KSHlBLo6aJaF32sj164dvXYXhlm0yR1oLdL3o6cEXxKFwDh4zsLzjSVCd02ZVCFfT45TF76S7bSCSSfWiq2bnYkQ+dadV02VqhEVkOpuej3GIye7GIC8XJAEKmWBOg9GjgTxGPfNpZ7IyFzzuaZGi7CfexdTgyrruFP+RtkRispqw1fayFD0CBbhd0ifvoZuwcvRtB9HwDaoOI3Btd3Vt+NgnJ3Rz1erFQUZlGKOmmCtxGOAtcBo4DXW922ZCRdV9cfZHMD5eNPdg2EpIO3W/zzW46z4kTw1VeV7M3cEz3OgAT0DZfRoQSNf05GkbuE2nqXCqZt2BG51Hue7OmnzmgkekuWqUsVCc9/ImtycVI118zRptUTXQo7di532uZoayP6CM8d+7mPKnLzrT9vp47c0ikVqfgV91j8UTnbuC6KyXSQ59KOe3wjuuRFfgfKOoxd0x2CjF23wGFC4oQTZJj3rM9BAeKEzo/mYKenYc7HLqmf42hmGtCbRgoU6TNv5FhtPvc/D3P8ch6ZeEw3XdQpngWK6jVT3YqtV1b4MjIE9MsHFAjIW+RiZYul7TFLynGIxI+Qtwemx3YSiJ5tblwLyTFIZ8T2izG9YxKCRkgRHNvXwp0K9+EwcN/dNhwtftRiEEWpw7TU7zEK1QF6yWGPZ1JD45RmJQPdxCXb7D0eQMsOHMKN6vEb6T8MX3aEibRArAcNuR3zKabXCCuCiXMN+GG/hwAka5jFdt2ZpD596xyizVzirQgUHx/zeivyEKItJKm7drzbae6m4+fbOlzhBm7nLcD+Myfcf1zw13Dcg+pbZn0Z7DAhVlU1iCpktHa6UstjyXODMgba1FBGdDCx99KojaKVqqQrJLn7+KMsgssgCktm+blGvoKTtTCR74/xnRV8C3fUPZu12xKAyiLIp9VzZUNZXyU4PyR6X7kGqNncBzcltfNYxUdK/05HTPODjgH19Ccuhg2Al1umC5v56QZfjDd2+M+Ss8m2JQbOzEFbKwJgmxn5Qb7jTlWJxM0M5ZIlI6k1IgrZM7QTQqnKL4xcC4xOxlHzlOx38TuueF+BoX6gW1iO3NExVjxYu5PlcdHLdyLFryLQAQCQm1NZXvNxvhzra2kpuYB9QWURVHP8ko0go5c6gPr8NyZrWXmBTadteY0m+q2Z440cNG1Xi0iJschv+2ZAsKivHbBEhDpPE+ZtLQIuU5zahV04gpBWJm7iX0MhFNIjX9l8EeYRNosvkoJiTJ1YCTL1BmdulpNv3qgeBPBwTtGMDZIhUKZ55ZRQFWSVWbdH2Z0ymrlZiUPvBrtb7NkDjtu2XI86a8bduXVCuXV9Ed5hiv33657L/qtcJh7x42Y6Ni23N/U6cpwkLFtr5y/6zmXTSFgU9e28zlrvgwxH08/madcgn5xysIxk8th7aAAiPPWV3PW59MkmlR0asALotKN+vZlkvT37KWQWu0ZOdaJifAgsZIRpA98kg9MhP2ip7heyRFWcwvKbjPPghETq9cHXgTvLpl09u0gaS6P5uRrVYnKwDrqpogWmqmh5SVzLNuIWkmrDtzqG+7AbrnJKNtkIp/RJOjcW6khGiAR7/CHiHYBerZTF8Xwjq0Uk0sx8+LeYvNwfsQUXGlSjVMXdYQ6EKqydg1VoIXbAvNRSFlCSddXejgL7AsOVrm6WNrzHJXGMvdmIvUCfYA1GqmC3DQs/vqGGjmJ3CljEhMColL2gk1hGmBTwOEf1wWdheslfRaOy89nfw4RqoCIR/sJzN18U8fSl/vowJSFxsraQAR9rEwXp+lxyrAt+6kwFsKG210vB+bQZl/EnC2ekTkdNaFko7Bos/a0ysOLy3E7ybFUbli9+75HIjXyUw+eHDTrzoTgCzq3fYUf6wrUCBpcENNevsg8Ig09Cwer7fPcDcV4VPKNeQ7HlgdBB1msOZjGMZkiLcCx7Ktz5S9HFt4EFJkYF5rjeyxBZifIFDJlwNj2nV+d7Lx2fSpI5DQPapAf7coibKKRL8AjTDyKyRQ2O0ooNBDcwceHmVrdI9gA4QqdAMv40g6Bp5qOW3I9fsnRsayABTkHXotzFVHNshV4Kyv7WvHHNMsjTgr7PIPPTfOGR6w/epH3pZf+mQ8s7ueadp12G6h3AYeR96nu4bBedVJRw4TQiXwMJdxWlXHYAfzIbHGsQqUYb/8WfvITtYlQbMUD2/wrB/FVgNKI/ut0Y4aMqoOBIKa22Voedm4+/RJ9ZJ2IWBPXcZCbtVMYk3RjsnLUjvYykt2/TES+LRl/gTrALMVl4l9UgfeCYzOUDNP8fM+zLYXVIAIUXjDHbVh7Hv4CpS/zDuuViUjJUdGLyvwgLq8qIyL2M5mCvaHG7dwZ7Qi3yAKQHREkN3VhEfagRnqKW2HRJqCD8xcc2IxHPv40pdG1QrRmMCsiiJFbMQhFaUwtp8RYn4+Bk7ddRrI/L/YftAgIt6ADkq67OJbtmfe0pm9ecxpsirrR/MwvjvGS9Hd8ivnUxaXks418ta2kkhIlwne+PtZ+Fo6NhhyK4poGxHnr7Z0uYTj/zv2X7MwGFsdt1vKmIYv3OiH4GZCuq46rnrGiEG7CNq7IRYQtsM2E+oEqyOYRuyD25meted1eExXiFgkrdPVHTqMy3cAs8qr1xIuayRSCMpCMlfNQe85rrWURu4ILhYwryeKVlOIaWXZ5Encd2UffWMfwCbYobRs3pXJbjgtUsCtRHSsfnu+DIAVgkWC37pPhYBC00yQasE9u0gGbR2ThfDFTZtn4v4Z3IE8HNQACRY1aGAuoFHzhEsKu4lABCtZKkkZloQXggia486Och41wb4nIiv1DyWKO+/kQu3rIzDUpLFfrAzgABLdOI+RagjtX/91hEwQKUkPsGQvt8nuE79Z0bBKHT6RhciosBFFcDxhG09XrsENu6EEJq6hRh57QOdyx9A2RyA5ct1P0oQGKt40B53jnZ8qp8NYEfz50KShTx/4ZCclrD6duiD+fXzoSPBKSmNgvNQtk//YUrg4DeTDKGFgcdA4lWqKOOXGfImX87eRfbGufXA3W5HwoXpcPHnXbnotIweH/u03dvG7MlCq4yfw9zyTK1UzPf/TjBsioQnzwJ/1vZdt4RT+GgQT+fiXi9KGqWpnYSzu4TxOD930ZDo/UpyFTrb8GC5a/RedGBNfNbYk8r8BxABPDPznDdt83frDjJ38wdCmxTDpKq6Z7RHfU8n/rzlwRkv4phUVn335mDaNIfTAPBtL9zIkJS79gHfYh1b1YcbjPESTj3NsT1quBRV99zgWnIO6wlRfmOrc5BTS85sgcxoLv9emYV1alzOyyHfyK+Acf6TL09FoQgAhfc4y7gTzVfW8W9OxBtI6i+Sfm94SjG8nUMEEU7L8P/wQWibMC+mS2U+N39QsclVc53x32u4YjB/tify+F3O/+k0rU+6t9aR2THt/p6RDvCc3fHYV+cRbl6LD/5tfT+luruog1g3d847SfLPJO/OmOPzR0/PzRpDV47oMeTfTf/6rchyh0/f+Ovprr/xmUziu5EazdSzi63Ji/vuX3BWXC0ZV9for/AloTzTAqfkJ5AAAAAElFTkSuQmCC","key2":"2018-10-17 19:56:58","key3":"fc4f101ee9924c44de901294041f6df2","key4":"03","key5":"2"})
# a = {"key1":"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","key2":"2018-10-17 19:56:58","key3":"fc4f101ee9924c44de901294041f6df2","key4":"03","key5":"2"}
# imageBase64 =a['key1']
imageBase64 = '''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'''
imgdata = base64.b64decode(imageBase64)
image=io.BytesIO(imgdata)
img = Image.open(image).convert('L')

img.save('d:/dog.png')


plt.imshow(img) # 显示图片
plt.show()