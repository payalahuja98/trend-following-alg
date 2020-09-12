import numpy as np

'''We establish a strategy of trend following 
   (buying when price trend goes up, selling when price trend goes down.)
   If a market has an significant upward trend, we go long in the market.
   If it lacks this trend, we short the market.'''

def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    nMarkets= CLOSE.shape[1]

    #defines long and short time scale
    periodLong = 200
    periodShort = 40

    #calculates long, short avgs of close
    smaLong = np.nansum(CLOSE[-periodLong:, :], axis=0)/periodLong
    smaRecent = np.nansum(CLOSE[-periodShort:, :], axis=0)/periodShort

    #if recent moving avg is above long-term avg, 
    #then go long; otherwise, short the market
    longEquity = smaRecent > smaLong
    shortEquity = ~longEquity

    #equal weight placed on each market long/short
    pos = np.zeros(nMarkets)
    pos[longEquity] = 1
    pos[shortEquity] = -1

    weights = pos/np.nansum(abs(pos))

    return weights, settings


def mySettings():
    settings = {}

    #define markets to trade
    settings['markets'] = ['F_AD','F_BO','F_BP','F_C','F_CC','F_CD','F_CL','F_CT',
                            'F_DX','F_EC','F_ED','F_ES','F_FC','F_FV','F_GC','F_HG',
                            'F_HO','F_JY','F_KC','F_LB','F_LC','F_LN','F_MD','F_MP',
                            'F_NG','F_NQ','F_NR','F_O','F_OJ','F_PA','F_PL','F_RB',
                            'F_RU','F_S','F_SB','F_SF','F_SI','F_SM','F_TU','F_TY',
                            'F_US','F_W','F_XX','F_YM','F_AX','F_CA','F_DT','F_UB',
                            'F_UZ','F_GS','F_LX','F_SS','F_DL','F_ZQ','F_VX','F_AE',
                            'F_BG','F_BC','F_LU','F_DM','F_AH','F_CF','F_DZ','F_FB',
                            'F_FL','F_FM','F_FP','F_FY','F_GX','F_HP','F_LR','F_LQ',
                            'F_ND','F_NY','F_PQ','F_RR','F_RF','F_RP','F_RY','F_SH',
                            'F_SX','F_TR','F_EB','F_VF','F_VT','F_VW','F_GD','F_F']

    #define time period to evaluate
    #settings['beginInSample'] = '20190101'
    #settings['endInSample'] = '20191231'

    #look more into "lookback period"
    settings['lookback'] = 504

    settings['budget'] = 10**6
    #slippage: difference between the price at which you expected or placed your order
    #and the price at which your order was actually filled
    settings['slippage'] = 0.05

    return settings

if __name__ == "__main__":
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)

