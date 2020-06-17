data = {
    "root":"/data/JDE",
    "train":
    {
        "mot17":"./data/mot17.train",
        "caltech":"./data/caltech.train",
        # "citypersons":"./data/citypersons.train",
        "cuhksysu":"./data/cuhksysu.train",
        "prw":"./data/prw.train",
        "eth":"./data/eth.train"
    },
    "test_emb":
    {
        "mot15":"./data/mot15.val"
    },
    "test":
    {
        "mot15":"./data/mot15.val"
    }
}




if __name__ == '__main__':
    import mmcv
    data = mmcv.Config(data)
