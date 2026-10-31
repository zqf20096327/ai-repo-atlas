# GAIR-NLP/AcademiClaw

⭐ 20 · C · NOASSERTION · 推送 2026-06-26 · [GitHub](https://github.com/GAIR-NLP/AcademiClaw) · [官网](https://gair-nlp.github.io/AcademiClaw/) · 组织维护 · 中文 README

**评测 AI agent 的双语学术基准：80 道本科生真实任务**

双语（英/中）agent 评测基准：80 道任务全部来自本科生真实学术工作且已被主流 AI 编程 agent（Claude Code、Codex、Cursor）尝试但未独立完成，从 230 份投稿经两轮专家评审筛选，覆盖 6 类别与 25+ 领域；其中 64 道 CPU-only、16 道 GPU 必需。每道任务在双层 Docker 镜像的隔离沙箱中运行，用 6 种互补技术（模式匹配、代码执行、LLM-as-Judge、视觉 LLM、浏览器端到端测试、结构化输出校验）按 3-6 维度打 0-100 分，75 分判通过，并附五类安全审计与六个前沿模型的完整评测轨迹。仓库提供 run_in_docker.sh、build_all_images.sh、batch_eval.sh 等脚本，支持 Claude Code、任意 OpenAI 兼容端点（openclaw）与手动三种 agent 后端。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 80 道双语任务（49 英文 + 31 中文原生任务），源自真实本科生学术工作
- 双层 Docker 镜像隔离沙箱运行，依赖固定，GPU/CPU 任务自动路由
- 六种互补评分技术 + 五类（S1-S5）安全审计，统一 0-100 分制
- 附带六个前沿模型的完整消毒后对话轨迹与评分数据

## 适用场景

- 评测自家 agent 模型在真实学术任务上的完成率
- 对比不同前沿模型的分领域能力差距与安全表现
- 研究 agent 的工具使用模式与 token 成本效率

## 场景标签

`模型评测` `科研工具` · 领域:评测与运维

## 证据(README 行号)

> L27: AcademiClaw is a bilingual (English + Chinese) benchmark designed to
> L34: From **230 student-submitted candidates** a two-round expert review
> L40: Experiments on six frontier models show that **even the best one solves

## 星数曲线

```mermaid
xychart-beta
    title "GAIR-NLP/AcademiClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `50e9ec0d5daa` · [字段定义](../../DATASET.md)*
