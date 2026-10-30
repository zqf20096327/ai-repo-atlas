# suncloudsmoon/quizzer

⭐ 21 · Python · MIT · 推送 2026-04-06 · [GitHub](https://github.com/suncloudsmoon/quizzer) · [官网](https://pypi.org/project/quizzer-ai/) · 个人维护

**把 PDF 变成终端里 Duolingo 式测验课程的 CLI 学习工具**

面向个人学习者的 Python CLI 工具：读取 PDF 教材/讲义，将每页渲染为图像交给视觉 LLM 生成课程（course.json），提供 7 种题型、SM-2 间隔重复调度、自适应难度、脚手架式由识别到自由回忆的进阶，以及答题后基于原页图像上下文的多轮导师对话。带 XP/连胜/课程解锁等游戏化机制。需用户自备 OpenAI 兼容端点（本地或远程），依赖 LlamaIndex、PyMuPDF 等；长书籍生成课程可能耗时 12 小时以上。要求 Python 3.14+。

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

- PDF 生成完整课程，含 7 种题型
- SM-2 间隔重复与自适应难度调度
- 答题后可进入带源页图像上下文的 LLM 导师对话
- 兼容任意 OpenAI 兼容 API 端点（本地或远程）

## 适用场景

- 把教材/讲义 PDF 转成可练习的测验课程备考
- 通过间隔重复在遗忘临界点复习知识点
- 答错时即时与 LLM 导师讨论该题

## 场景标签

 · 领域:教育/学习工具

## 证据(README 行号)

> L7: Quizzer turns PDFs into interactive, Duolingo-style courses you can study from the terminal.
> L75: 1. **Course generation** (`/create`): Renders each PDF page as an image, sends it to a vision-capable LLM to triage

## 星数曲线

```mermaid
xychart-beta
    title "suncloudsmoon/quizzer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4f00a0364c19` · [字段定义](../../DATASET.md)*
