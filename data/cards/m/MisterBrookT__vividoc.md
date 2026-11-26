# MisterBrookT/vividoc

⭐ 10 · HTML · MIT · 推送 2026-06-09 · [GitHub](https://github.com/MisterBrookT/vividoc) · [官网](https://vividoc.vercel.app) · 个人维护

**把任意主题生成单文件可交互教学 HTML 文档的工具**

ViviDoc 接受单个主题输入，生成自包含的交互式 HTML 教学文档：自动设计视觉风格，按 SRTC（State·Render·Transition·Constraint）交互规范组织结构，输出含 KaTeX 公式与 Canvas 可视化的单个 .html 文件，无需构建步骤或服务器。它以 Claude Code 等编程 agent 为运行载体，命令安装到 ~/.claude/commands/ 下，提供 /vividoc、/vividoc-learn、/vividoc-slides 三个命令。附 ACL 2026 Demo 论文与展示站点，含 4 个领域 8 篇示例文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单文件 HTML 输出：KaTeX 数学公式 + Canvas 可视化，无构建步骤、无服务器
- SRTC 交互规范（State·Render·Transition·Constraint）组织文档结构
- 三个命令：/vividoc（主题生成）、/vividoc-learn（URL 改写）、/vividoc-slides（讲稿生成）
- 无需单独 API key，以 AI 编程 agent 作为运行载体

## 适用场景

- 把傅里叶变换等抽象概念做成可探索的交互式教学页
- 把已有教学网页或讲义 PDF 转成交互文档/幻灯片
- 为机器学习、信息论等课程制作课堂演示材料

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L14: ViviDoc generates **self-contained interactive HTML documents** from a single topic input. It designs a purpose-bui
> L24: Installs `/vividoc`, `/vividoc-learn`, and `/vividoc-slides` into `~/.claude/commands/`. Your harness is the model 
> L16: > **Accepted at ACL 2026 System Demonstrations** — arXiv:2603.01912


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `7dea50505ed4` · [字段定义](../../DATASET.md)*
