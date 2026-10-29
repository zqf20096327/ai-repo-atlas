# OpenVoiceOS/ovos-buildroot

⭐ 283 · Python · Apache-2.0 · 推送 2026-10-03 · [GitHub](https://github.com/OpenVoiceOS/ovos-buildroot) · 组织维护

**基于 Buildroot 的精简 Linux OS，将 OVOS 语音助手带到嵌入式设备**

OpenVoiceOS 项目维护的 64 位精简 Linux 发行版构建工程：以 Linux 6.1.x LTS 内核与 Buildroot 2023.02.x 为基础，通过 ovos-docker 容器打包 OVOS 语音助手框架，面向嵌入式、低规格无头设备与小型触屏设备。支持树莓派 3/3b/3b+ 与树莓派 4（UEFI 方式），x86_64 支持标注为进行中，另支持 Open Virtual Appliance。文档位于 documentation 目录，采用 Apache 2.0 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Buildroot 2023.02.x LTS（含本地修改）构建的精简 64 位发行版
- OVOS 框架经 ovos-docker 容器打包（当前为 alpha/开发版）
- 支持 Raspberry Pi 3/3b/3b+ 与 Pi 4，x86_64 为进行中

## 适用场景

- 在树莓派等低规格设备上运行 OVOS 语音助手
- 为无头或小触屏嵌入式设备构建语音助手系统镜像
- 以虚拟机（OVA）形式试用 OVOS 环境

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: This is a minimal Linux OS for ovos-core, the open source voice assistant. It runs on embedded devices, low-spec hea
> L11: - The OVOS framework, packaged through ovos-docker containers (currently the latest alpha/development version)

## 星数曲线

```mermaid
xychart-beta
    title "OpenVoiceOS/ovos-buildroot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 282 --> 284
    line [283, 283]
```

2026-10-18 283 → 2026-10-29 283（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `5642944075d7` · [字段定义](../../DATASET.md)*
