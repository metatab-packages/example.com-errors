import metapack as mp



def test_package():
    import warnings
   
    warnings.simplefilter("once", UserWarning)
    
    pkg = mp.jupyter.open_package()
    
    try:
        from pandas.arrays import IntegerArray
        # If we  have an IntegerArray avilable in pandas, it should all work great
        with warnings.catch_warnings(record=True) as wlist:
        
            nn = pkg.resource('numbers_and_nulls').dataframe()
        
            for w in wlist:
                if w.category is UserWarning:
                    assert False, "Should not have gotten a warning"
                    break
                    
            else:
                pass
        
        
    except ModuleNotFoundError:
        # If we don't have an IntegerArray avilable in pandas, we should get a warning
        with warnings.catch_warnings(record=True) as wlist:
        
            nn = pkg.resource('numbers_and_nulls').dataframe()
        
            for w in wlist:
                if w.category is UserWarning:
                    print(w)
                    break
            else:
                assert False, "Didn't get the warning that was expected"
            

    
if __name__ == "__main__":
    test_package()   
    