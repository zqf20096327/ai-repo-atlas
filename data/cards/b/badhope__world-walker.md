# badhope/world-walker

⭐ 16 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/badhope/world-walker) · [官网](https://badhope.github.io/world-walker/) · 个人维护 · 中文 README

**给 AI Agent 调用的确定性文字互动游戏规则内核（MCP+CLI+只读面板）**

世界观无关的文字互动游戏规则引擎：命中、伤害、交易、势力消长、谣言传播等全部由确定性规则函数结算，语言模型只负责把 JSON 状态转写为叙事，不得编造数值。对外提供 MCP 服务器（stdio，39 个工具）、14 条命令的 CLI 与离线只读网页主舞台三条通道，共用同一状态文件；同一种子逐字节可复现。附带四套设定包（玄幻/武侠/赛博朋克/悬疑），支持 SillyTavern 角色卡与世界书导入。本体检零第三方依赖，不调用任何模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 144 个规则函数确定性结算，同种子逐字节可复现
- 39 个 MCP 工具（stdio）+ CLI + 只读网页面板三通道
- 四套设定包演示四种玩法循环（freeform/choice/mud/ttrpg）
- 兼容 SillyTavern 角色卡（PNG/JSON V1–V3）与世界书语义

## 适用场景

- 让 Claude Code/Cursor 等 Agent 主持长线文字冒险或跑团
- 换设定包快速搭建不同世界观的 AI 互动叙事
- 需要数值可核对、可回退存档的确定性 AI 文字游戏

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L20: - **Agent 作文**：语言模型只把你看到的 JSON 转写成文学描写，不得编造数值；
> L307: 不需要。它不调用任何模型；模型由你的 Agent 提供。引擎只负责"世界怎么变"。

## 星数曲线

```mermaid
xychart-beta
    title "badhope/world-walker 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 14 --> 17
    line [15, 16, 16]
```

2026-10-18 15 → 2026-10-30 16（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `a7f18ea6ecae` · [字段定义](../../DATASET.md)*
