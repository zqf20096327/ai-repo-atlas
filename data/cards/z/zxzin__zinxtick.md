# zxzin/zinxtick

⭐ 25 · 推送 2026-05-31 · [GitHub](https://github.com/zxzin/zinxtick) · 个人维护 · 中文 README

**把角色/产品/日常物品变成主题贴纸包的 AI agent 技能**

以 SKILL.md 指令文件夹形式提供的 agent 技能：给定一个角色、动物、产品或物品，引导 agent 走完主体身份锁定、风格/主题预设选择、逐张贴纸反应规划、图像生成提示词、整包 QA 与平台级素材导出的流程；无图像生成模型时输出可直接使用的提示词包而非伪造成品图。面向支持本地技能或可复用指令目录的 agent（Claude 风格、Antigravity 风格、Codex 等），复制仓库到技能目录后以 $zinxtick 调用。提供 6 种风格预设与 7 种主题预设，中英文输入分别使用对应预设菜单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整贴纸包工作流：主体锁定→预设选择→逐张规划→提示词→QA→导出
- 无图像生成模型时产出 generator-ready 提示词包
- 6 种风格预设与 7 种主题预设，中英文双语菜单适配

## 适用场景

- 给我的 AI agent 加上生成贴纸包的能力
- 为聊天表情、吉祥物或产品周边制作成套贴纸
- 没有本地生图模型时先拿到整套生成提示词

## 场景标签

 · 领域:AI agent 技能/创意生成

## 证据(README 行号)

> L3: Zinxtick is an AI agent skill for turning a character, animal, product, food, drink, can, object, mascot, or visual 
> L5: It is designed for agents that support local skills or reusable instruction folders, including Claude-style agents, 
> L66: If your agent does not support `$skill` syntax, point it at `SKILL.md` and ask it to follow the Zinxtick workflow.

## 星数曲线

```mermaid
xychart-beta
    title "zxzin/zinxtick 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `b851b44d378d` · [字段定义](../../DATASET.md)*
