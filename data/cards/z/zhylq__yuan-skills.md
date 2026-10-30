# zhylq/yuan-skills

⭐ 35 · TypeScript · MIT · 推送 2026-03-13 · [GitHub](https://github.com/zhylq/yuan-skills) · 个人维护 · 中文 README

**面向 AI 编码工具的公众号写作 Agent Skills 仓库**

为 OpenCode、Claude Code 等支持 SKILL.md 的 agent 工具提供的技能仓库，含 1 个主写作 skill（zhy-wechat-writing，覆盖公众号文章的检索、证据池、初稿、审稿、润色与后处理编排）与 3 个可选辅助 skill（配图生成、Markdown 转公众号内联 HTML、上传公众号草稿箱）。通过 npx skills add 安装，可选功能需配置图像生成通道、七牛云或微信公众号 API 凭据。

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

- 主 skill 覆盖检索、证据池、初稿、审稿、润色的写作编排流程
- Markdown 转微信公众号内联 HTML 并上传草稿箱的辅助 skill
- 支持仅装主 skill、加转 HTML、完整链路三种使用模式
- 可选图像生成通道包括 OpenAI / Gemini / 小米等 API

## 适用场景

- 让 Claude Code 等 agent 按流程撰写微信公众号文章
- 自动为文章配图并转为公众号可用 HTML
- 一条龙完成写作、配图、转换并保存到公众号草稿箱

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: 一个面向 OpenCode、Claude Code 等 AI 编码工具的 Agent Skills 仓库，适配：
> L55: - `zhy-wechat-writing` - 主写作 skill，负责公众号文章的检索、证据池、初稿、审稿、润色与可选后处理编排

## 星数曲线

```mermaid
xychart-beta
    title "zhylq/yuan-skills 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cec0fadfadb1` · [字段定义](../../DATASET.md)*
