# Mijiang111/SylvaDeck

⭐ 18 · TypeScript · MIT · 推送 2026-05-03 · [GitHub](https://github.com/Mijiang111/SylvaDeck) · 个人维护 · 中文 README

**本地优先的 HTML AI 演示文稿创作工作台，可导出 PPT**

面向演示文稿制作者的本地 Web 工作台：从自然语言 brief 生成 1600x900 固定画布的 HTML 幻灯片，内置布局/标题溢出/密度的预检与修复流程，结果在 iframe Studio 中保持可编辑，可导出 HTML 与 .pptx。核心机制是 Agent Bridge：给编码 agent 安装技能后通过本地 bridge API 把任务交给真实浏览器会话中的 Studio 生成。需 Node 20+/pnpm 9+ 及本地 AI agent 环境，状态为 alpha，面向单机使用而非云部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自然语言 brief 生成 1600x900 固定画布的 HTML 幻灯片
- Agent Bridge：agent 经本地 bridge API 在真实产品会话中启动生成
- 布局/标题溢出/密度预检与修复（preflight/repair）
- 导出可发布 HTML 与可编辑 .pptx

## 适用场景

- 用已有的编码 agent 通过对话生成可编辑的演示文稿
- 在本地工作台中创作模板并迭代生成质量
- 把结构化思考产出为 HTML/PPT 双格式成品

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L4: Claw Design is a local-first, HTML-based AI presentation workbench with an Agent Bridge, letting you create Claude-l
> L78: - Generates slide-like HTML reports from a raw brief
> L169: User inputs requirements in the **UI** → **Server** assembles prompt → calls **local AI Agent** to generate HTML →

## 星数曲线

```mermaid
xychart-beta
    title "Mijiang111/SylvaDeck 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `2837672a59a2` · [字段定义](../../DATASET.md)*
