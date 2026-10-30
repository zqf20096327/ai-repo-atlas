# Jinsong-Zhou/xhs-autopilot

⭐ 20 · Python · MIT · 推送 2026-02-12 · [GitHub](https://github.com/Jinsong-Zhou/xhs-autopilot) · 个人维护 · 中文 README

**面向小红书创作者的 AI Agent 内容创作全流程自动化技能**

基于 Claude Code Skill 构建的小红书内容创作自动化项目：通过 /xhs-creator 技能调用 Claude Code 与 xiaohongshu-mcp，完成竞品搜索、爆款模式分析、内容撰写、封面生成（Pillow 或 HTML+Playwright 截图）与一键/定时发布。面向使用 Claude Code CLI 的内容创作者，需 Python 3.13+、uv，并单独下载配置 xiaohongshu-mcp 与登录小红书账号。README 列出标题 20 字、正文约 1000 字等平台限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 竞品多维搜索与爆款标题/内容结构/标签模式分析
- 基于分析结果生成符合平台调性的原创内容
- 封面两套生成方案：Pillow 批量 / HTML+Playwright 截图
- 支持立即与定时发布，自动填充标题正文标签封面

## 适用场景

- 调研小红书竞品并提取爆款内容模式
- 让 AI Agent 生成并直接发布小红书笔记
- 批量生成符合平台尺寸限制的封面图

## 场景标签

`AI 写作` `图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: > 小红书内容创作自动驾驶 — 基于 Claude Code Skill 的 AI Agent 全流程自动化
> L10: 从竞品调研到一键发布，让 AI Agent 帮你完成小红书内容创作的每一步。

## 星数曲线

```mermaid
xychart-beta
    title "Jinsong-Zhou/xhs-autopilot 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-30"]
    y-axis "stars" 18 --> 21
    line [19, 20, 20]
```

2026-10-18 19 → 2026-10-30 20（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d6e73e92dd1d` · [字段定义](../../DATASET.md)*
