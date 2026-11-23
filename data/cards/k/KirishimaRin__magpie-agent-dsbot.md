# KirishimaRin/magpie-agent-dsbot

⭐ 3 · JavaScript · MIT · 推送 2026-10-25 · [GitHub](https://github.com/KirishimaRin/magpie-agent-dsbot) · 个人维护 · 中文 README

**让 DS-Bot 使用 Magpie 模型目录与路由组的同步插件**

KirishimaRin 开发的第三方 Magpie 插件，将用户在 Magpie 中配置的供应商模型与路由组接入 DS-Bot：按用户模型目录持续同步模型、能力（上下文、输出预算、图片输入、思考档位）与协议识别（Chat/Responses/Anthropic，支持手动覆盖与默认回退）。请求链路为 DS-Bot → Magpie 网关 → 供应商，API Key 由 Magpie 管理。运行要求 Windows、已配置模型的 Magpie 与 DS-Bot 桌面版；诊断命令需 Node.js 22+。插件保留原有供应商与 Bot 设置，提供诊断、清理与升级兼容入口。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步 Magpie 模型目录与路由组，保留显示名称
- 同步模型能力：上下文、输出预算、图片输入、思考档位
- 自动识别 Chat/Responses/Anthropic 协议，支持手动覆盖
- 提供诊断（npm run check / explain）与断开清理、升级兼容入口

## 适用场景

- 在 DS-Bot 中直接选用 Magpie 已配置的模型与路由组
- 模型供应商或协议变更后同步更新 DS-Bot 的模型配置
- 不修改 DS-Bot 安装文件的前提下接入自建模型网关

## 场景标签

 · 领域:LLM 基础设施/模型接入工具

## 证据(README 行号)

> L3: 让 **DS-Bot 使用 Magpie 中已配置的供应商模型和路由组**，同步模型能力与思考强度选项。
> L53: 插件使用 Magpie 提供的上下文、输出上限、图片输入和思考档位，交给 DS-Bot 内置适配器使用。实际请求沿 **DS-Bot → Magpie 网关 → 模型供应商或路由组** 转发。

## 星数曲线

```mermaid
xychart-beta
    title "KirishimaRin/magpie-agent-dsbot 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `a8309f9d8201` · [字段定义](../../DATASET.md)*
