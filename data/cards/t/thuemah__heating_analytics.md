# thuemah/heating_analytics

⭐ 15 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/thuemah/heating_analytics) · 个人维护

**Home Assistant 集成：机器学习预测供暖能耗并检测浪费**

面向 Home Assistant 用户的自定义集成（经 HACS 安装）。它学习住宅室外温度、风力、日照与供暖/制冷能耗之间的关系，逐小时预测当前天气下应有的能耗并与实际值对比，输出偏差告警（如开窗散热）、辅助热源（壁炉/取暖器）节能量估算、逐区效率追踪与最长 7 天的能耗预报。定位为前馈诊断引擎，不直接写设定值或控制设备，输出供 HA 自动化、EMHASS、Node-RED 等外部逻辑使用。模型需 7-14 天多样天气数据完成校准；要求能耗表为稳定的累计 kWh 计数器，并需配置天气实体。支持 CSV 历史数据导入加速训练，提供 Track A/B/C 三种学习模式（含配合 heatpump_mpc MPC 负荷转移的热力学基线模式）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐小时学习住宅热工特性并预测应有能耗，偏差告警
- 从壁炉/取暖器等辅助热源中分离节能量
- 多区域（逐房间/逐供暖单元）效率追踪与基线
- 前馈设计：只产诊断与预测，不直接控制设备
- CSV 历史数据导入可即时完成训练

## 适用场景

- 发现开窗散热等供暖能耗异常并收到告警
- 量化壁炉或电暖器带来的实际节能量
- 基于天气预报查看未来 7 天的供暖能耗预测
- 配合热泵 MPC 控制器追踪真实效率（Track C）

## 场景标签

 · 领域:智能家居/能源监测

## 证据(README 行号)

> L26: The integration continuously learns the relationship between outdoor conditions (temperature, wind, sun) and your h
> L160: - **Automatic Learning (Track A):** No manual calibration needed—the system learns your home's thermal characteris

## 星数曲线

```mermaid
xychart-beta
    title "thuemah/heating_analytics 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-31 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `8f95780375df` · [字段定义](../../DATASET.md)*
