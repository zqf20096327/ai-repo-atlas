# miguelmartens/opencode-gearbox

⭐ 4 · TypeScript · MIT · 推送 2026-11-13 · [GitHub](https://github.com/miguelmartens/opencode-gearbox) · [官网](https://getgearbox.dev) · 个人维护

**OpenCode 插件：按提示自动选推理档位与子代理模型**

为 OpenCode V2 提供的插件，通过一个小型 judge 模型为每条主对话提示评级（low 到 max 五档），并将该档位套用到请求的 effort variant 上；同时为每个子代理分配独立档位，并按提供商价格梯度选择更便宜的模型。内置状态栏显示决策与理由、会话成本统计、节省模式与每日预算、基于 135 条标注提示的 judge 基准测试。要求 OpenCode V2 2.2.6+，不支持 Claude Code，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- judge 模型按提示自动分配五档推理档位，状态栏展示决策原因
- 子代理按价格梯度自动分配更便宜模型与独立档位
- /gearbox bench 基于标注提示集评分 judge 模型
- 支持每日花费预算与节省模式自动降档

## 适用场景

- 在 OpenCode 编码工作流中按任务难度自动调整推理档位以控制成本
- 让子代理在简单任务上使用更便宜的模型
- 按会话统计 token 与花费并设置每日预算

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7:  Automatic transmission for OpenCode.
> L40: Gearbox is built for **Claude models** first; other models with effort variants work too (see Supported models). It
> L119: Add the package to the `plugins` list of your global (`~/.config/opencode/opencode.jsonc`) or project `opencode.js

## 星数曲线

```mermaid
xychart-beta
    title "miguelmartens/opencode-gearbox 星数(近 3 点)"
    x-axis ["2026-11-11", "2026-11-12", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-11 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `3788956cc975` · [字段定义](../../DATASET.md)*
