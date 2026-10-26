# irenerachel/comic-ip-onboarder-skill

⭐ 67 · 推送 2026-06-19 · [GitHub](https://github.com/irenerachel/comic-ip-onboarder-skill) · 个人维护 · 中文 README

**把照片或吉祥物转成可复用漫画 IP 档案的 Agent Skill**

以 SKILL.md 格式发布的 AI Agent 技能：在支持 skills 的 agent 环境中安装或复制后使用。流程为从照片、头像、玩偶、手办或吉祥物中提取身份锚点，生成正面全身确认图、三视图与固定 8 张独立表情动作参考图，最终整理成 IP_DNA.md 档案，可交给下游漫画信息图工作流复用。仓库仅含 SKILL.md 与 IP_DNA 模板，不含用户资产与密钥，提示词默认使用中文。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定义三阶段流程：确认图→三视图→8 张独立表情动作参考图
- 产出 IP_DNA.md 档案供下游漫画/配图工作流复用
- 内置质检规则（禁止拼贴切分、禁止网页截图伪装成品图）

## 适用场景

- 把真人照片或玩偶做成风格化漫画角色档案
- 为漫画工作流建立可复用的新角色 IP 档案
- 基于已确认三视图批量生成表情动作参考包

## 场景标签

`提示工程` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L3: 把照片、头像、毛绒玩具、手办、品牌吉祥物或角色设定，转成可复用漫画 IP 档案的 AI Agent Skill。
> L39: 把这个仓库作为 skill 安装或复制到支持 skills 的 agent 环境中，保持下面的目录结构：

## 星数曲线

```mermaid
xychart-beta
    title "irenerachel/comic-ip-onboarder-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-26 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2bc6964d6306` · [字段定义](../../DATASET.md)*
