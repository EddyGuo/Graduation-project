from zentao_intranet import InZenTao


inZT_driver1 = InZenTao()
inZT_driver1.bug_search_case1('P系列/P1pro', inZT_driver1.xpath.search_value1_chosen2)
inZT_driver1.driver.close()
inZT_driver2 = InZenTao()
inZT_driver2.bug_search_case1('P系列/P1pro_一体播控')
inZT_driver2.driver.close()
