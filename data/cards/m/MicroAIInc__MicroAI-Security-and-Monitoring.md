# MicroAIInc/MicroAI-Security-and-Monitoring

⭐ 60 · Python · NOASSERTION · 推送 2025-12-11 · [GitHub](https://github.com/MicroAIInc/MicroAI-Security-and-Monitoring) · [官网](https://security.micro.ai) · 组织维护

**嵌入式设备端 AI 安全与监控 agent：在设备上训练并运行安全算法**

MicroAI Security & Monitoring 是部署在边缘设备上的安全监控 agent，将安全算法嵌入并在设备、机器或进程上直接训练与运行，用于异常检测与设备监控。安装以预编译二进制包（Linux x64/ARM、Windows x64）或 Docker 镜像方式提供，运行需通过 MicroAI Launchpad 激活许可证并以 license key 启动。可选本地 UI Console（需 Java 17），支持配置目录与日志目录挂载；容器模式要求 --privileged 与 --net=host。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 算法直接在设备端嵌入并训练，无需云端模型调用（README 声明 Edge-native）
- 提供 Linux x64/ARM、Windows x64 预编译安装包与 Docker 镜像
- 许可证 key 激活后以单命令运行，可选本地 UI Console（端口 8989）
- 提供进程/日志/版本三类安装后验证步骤

## 适用场景

- 在工厂设备或 IoT 终端上运行安全与异常检测 agent
- 通过本地 UI Console 监控 URL 与端口并配置告警响应
- 以容器方式在边缘主机部署安全监控 agent

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7:  MicroAI Security & Monitoring is an Edge-native AI platform that embeds and trains advanced security algorithms dir
> L9:  This guide will help you install , configure , and validate the MicroAI Security & Monitoring agent, ensuring it op

## 星数曲线

```mermaid
xychart-beta
    title "MicroAIInc/MicroAI-Security-and-Monitoring 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 59 --> 61
    line [60, 60]
```

2026-10-18 60 → 2026-10-27 60（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `7854a19d11af` · [字段定义](../../DATASET.md)*
