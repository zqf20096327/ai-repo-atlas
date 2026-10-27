# AlexFengCisco/Telemetry_Receiver

⭐ 23 · Python · 推送 2026-01-05 · [GitHub](https://github.com/AlexFengCisco/Telemetry_Receiver) · 个人维护

**采集 Cisco NX-OS/IOS-XR 遥测数据的 Python 示例代码集**

面向网络工程师的 Python 示例代码：演示通过 UDP/TCP/gRPC（dial-in 与 dial-out）接收 Cisco NX-OS 与 IOS-XR 设备推送的遥测消息，并解析 JSON、GPB compact、GPB-kv 三种编码格式，附内部 MDT 头部字段说明与 proto 文件生成命令。另含 MDS 9000 SAN Analytics 遥测采集示例与配置片段，以及一个基于 LSTM、多元高斯分布和亲和传播聚类的遥测机器学习示例引擎。测试环境为 N9K 与 XRv9K。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- UDP/TCP/gRPC dial-in 与 dial-out 两种模式接收遥测
- 解析 JSON / GPB compact / GPB-kv 编码并输出结构化结果
- MDS 9000 SAN Analytics 遥测采集示例与 MDS 9710 配置片段
- 示例机器学习引擎：LSTM 预测、多元高斯异常检测、亲和传播聚类根因分析

## 适用场景

- 搭建自用的 Cisco 设备遥测接收端并解析消息
- 学习 GPB/GPB-kv 遥测编码与 gRPC dial-out 接入方式
- 在 SAN 环境中采集 MDS 交换机流量分析遥测数据

## 场景标签

 · 领域:网络运维/遥测采集

## 证据(README 行号)

> L3: ### Python Telemetry Receiver for collection Cisco NX-OS IOS-XR UDP/TCP/gRPC
> L5:  A Python sample code demo how to collect Telemetry mesasge via UDP/gRPC and how to Parse message.
> L179:  Sample telemetry machine learning engine code ,

## 星数曲线

```mermaid
xychart-beta
    title "AlexFengCisco/Telemetry_Receiver 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `5bcb620ed77a` · [字段定义](../../DATASET.md)*
