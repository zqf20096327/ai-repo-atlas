# enoch85/ovms-home-assistant

⭐ 33 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/enoch85/ovms-home-assistant) · 个人维护

**把 OVMS 电动车模块接入 Home Assistant 的 MQTT 集成**

面向 Home Assistant 用户的 OVMS V3 自定义集成：通过 MQTT 订阅 OVMS 模块发布的车辆指标，自动发现并创建传感器、二元传感器、设备追踪器与开关等实体，按电池、空调、位置等类别分组，支持向车辆发送带速率限制的指令。单位信息可向模块查询（固件 3.3.004+）而非按主题名猜测，提供电芯级统计、TPMS 胎压与 GPS 追踪。经 HACS 或手动复制文件安装，需自备 MQTT broker（支持 TLS/SSL），对 VW e-UP!、Smart、Nissan Leaf、Renault Twizy、MG ZS-EV 有专门支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动发现 OVMS 指标并创建实体（传感器/二元传感器/设备追踪器/开关）
- 向模块查询指标单位，固件更新新增指标无需更新集成
- 电芯级电池数据统计（最小/最大/均值/中位数）与偏差追踪
- 服务化车辆指令接口，带速率限制；支持 TLS/SSL MQTT 连接

## 适用场景

- 在 Home Assistant 中实时查看电动车的电池、空调、位置等指标
- 通过 Home Assistant 服务向车辆发送指令
- 追踪电芯电压/温度偏差与 TPMS 胎压，监测电池状态

## 场景标签

 · 领域:智能家居/车辆物联网

## 证据(README 行号)

> L4: The Open Vehicle Monitoring System (OVMS) integration for Home Assistant. Connect your electric vehicle with Home As
> L14: The OVMS integration discovers and creates Home Assistant entities from MQTT topics published by your OVMS module. 

## 星数曲线

```mermaid
xychart-beta
    title "enoch85/ovms-home-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-25 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `725f69c1d666` · [字段定义](../../DATASET.md)*
