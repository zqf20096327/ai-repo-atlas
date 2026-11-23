# khangdh0202/SillyTavern-Storyline

⭐ 4 · JavaScript · GPL-3.0 · 推送 2026-11-03 · [GitHub](https://github.com/khangdh0202/SillyTavern-Storyline) · 个人维护

**SillyTavern 扩展：AI 叙事者讲述你的角色故事**

为 SillyTavern 添加 storyteller 聊天模式的扩展：助手以连续叙事散文扮演世界叙事者，用户扮演主角输入行动。提供故事库（标题、开场、角色表、提示词，JSON 导入导出）、会话启动界面、按 token 预算智能注入相关角色、人称切换、骰子与记忆等可选功能。依赖 SillyTavern 1.18.0+，通过扩展面板以 Git URL 安装；三个配套扩展（角色状态/骰子/记忆）可选，缺失时功能照常运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 SillyTavern 官方 hook 重建整段生成提示词，叙事者无宿主卡片身份
- 按 token 预算相关性扫描注入近期提及的角色
- 故事库：每部故事为版本化、可导出 JSON 的定义
- 支持英文/越南语界面与每聊天人称切换

## 适用场景

- 在 SillyTavern 里玩文字冒险/互动小说，用户扮演主角
- 用骰子与角色表为故事加入 RPG 机制
- 管理多部带开场与角色设定的长篇故事

## 场景标签

`聊天机器人` `AI 写作` · 领域:对话与助手

## 证据(README 行号)

> L11: **Storyline** adds a new chat mode to SillyTavern: the assistant becomes the **Storyteller** — narrating the world 
> L75: - SillyTavern **1.18.0+**

## 星数曲线

```mermaid
xychart-beta
    title "khangdh0202/SillyTavern-Storyline 星数(近 2 点)"
    x-axis ["2026-11-08", "2026-11-23"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-08 4 → 2026-11-23 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `4d6e79ce19fa` · [字段定义](../../DATASET.md)*
