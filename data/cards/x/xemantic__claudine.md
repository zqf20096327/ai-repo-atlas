# xemantic/claudine

⭐ 179 · Kotlin · GPL-3.0 · 推送 2026-06-24 · [GitHub](https://github.com/xemantic/claudine) · 组织维护

**基于 Claude API 的自主 CLI AI 代理，用于学习 harness 工程**

以 Kotlin 编写的命令行 AI 代理，通过 Anthropic API 调用 Claude 模型，配备 5 个工具（读写文件、执行 Shell 命令、打开 URL），结合 Unix 命令行与互联网数据实现自主推理与行动，可编写并执行新工具扩展自身功能。作为 Xemantic agent AI 研究的一部分，同时用于教授 harness 工程的付费工作坊。需设置 ANTHROPIC_API_KEY，通过 Gradle 构建 JVM uberjar 运行，或在 Mac/Linux 上编译为原生二进制（Windows 原生构建暂缺）。GPL-3.0 许可，底层组件为 Apache 2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 5 个基础工具（文件读写、Shell 执行、打开 URL）驱动自主代理行为
- 可自行编写并执行新工具、修改自身提示词（元认知）
- 支持编译为 Linux/macOS 四平台原生二进制
- 基于 anthropic-kotlin-sdk 构建

## 适用场景

- 在自己的机器上通过对话完成文件分析、代码实现与系统管理
- 作为实现自主代理的蓝图，扩展 SQL 等领域专用工具
- 学习 harness 工程与代理系统设计

## 场景标签

`编码 Agent` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: Claudine reasons and acts autonomously while being Unix-omnipotent and having access to the internet, therefore it m
> L92: Claudine can _reason_, as much as Claude LLM can reason, so you can have any typical interaction like with a conver
> L94: * ReadFiles

## 星数曲线

```mermaid
xychart-beta
    title "xemantic/claudine 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 178 --> 180
    line [179, 179]
```

2026-10-18 179 → 2026-10-26 179（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `a5c59ae5f996` · [字段定义](../../DATASET.md)*
