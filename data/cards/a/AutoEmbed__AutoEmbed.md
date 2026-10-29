# AutoEmbed/AutoEmbed

⭐ 47 · Python · MIT · 推送 2026-06-12 · [GitHub](https://github.com/AutoEmbed/AutoEmbed) · [官网](https://autoembed.github.io) · 组织维护 · 中文 README

**面向通用嵌入式 IoT 系统的 LLM 自动化开发平台：自然语言到硬件验证代码**

Electron 桌面应用（后端 FastAPI），面向嵌入式 IoT 开发者：用户用自然语言描述任务并配置元件与引脚，系统通过 4 阶段流水线（库求解→知识生成→选择性记忆注入→自动编程）生成 Arduino 代码，调用 Arduino CLI 编译、烧录并在真实硬件上运行验证；内层编译-修复、外层烧录-验证双重反馈循环。从 7000+ Arduino 库动态发现并经 LLM 提取真实 API 以避免幻觉。支持 Arduino Uno/STM32 Nucleo/RP2040/ESP32 四平台、71+ 硬件模块，需自备任意 OpenAI 兼容 API key 与 Arduino CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 阶段流水线：自然语言任务到编译烧录并在硬件上验证的代码
- 从 7000+ Arduino 库动态发现并通过 LLM 提取真实 API
- 双重反馈循环：编译-修复内环与烧录-验证外环
- 支持 4 平台 71+ 硬件模块，任意 Arduino 兼容元件可用

## 适用场景

- 用自然语言描述需求，自动生成并烧录可验证的 Arduino 代码
- 在多种传感器/执行器组合的 IoT 原型上快速验证想法
- 借助真实 API 提取避免 LLM 编造库接口

## 场景标签

`代码生成` `编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L5: **LLM-driven Automated Software Development for Generic Embedded IoT Systems**
> L73: - **Natural Language → Deployed Code** — describe what you want, get compiled and verified Arduino code on real har
> L75: - **4-Stage Automated Pipeline** — Library Solving → Knowledge Generation → Selective Memory Injection → Auto-Progr

## 星数曲线

```mermaid
xychart-beta
    title "AutoEmbed/AutoEmbed 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 45 --> 48
    line [46, 47, 47]
```

2026-10-18 46 → 2026-10-29 47（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ef7853274e19` · [字段定义](../../DATASET.md)*
