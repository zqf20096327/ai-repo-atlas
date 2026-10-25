# romanticamaj/promptasy

⭐ 43 · JavaScript · NOASSERTION · 推送 2026-09-11 · [GitHub](https://github.com/romanticamaj/promptasy) · 个人维护 · 中文 README

**浏览器游戏：在离线 3D 世界中通过解谜学习提示工程**

基于 three.js/Vite 的网页游戏：玩家在程序生成的夜之世界中探索，通过拼组句子碎片构造提示来完成 142 个挑战。130 个教学神龛各教一项技能，内容取自 OpenAI、Anthropic、Google、xAI、Qwen、Mistral 等官方文档（446 条来源、339 个文档，多数深度链接到原文段落）。评分由 81 个规则检查组成的离线引擎完成，全程不调用模型、无后端、无账号，进度存于 localStorage。UI 为繁体中文，需 Node.js 18+ 通过 npm 构建运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 142 个挑战、130 项技能，内容逐条引用官方文档并可跳转原文
- 离线评分引擎（81 个检查，双语模式检测，支持部分得分与反刷分）
- 零模型调用、零后端、零外部请求，核心循环可在无网环境运行
- 支持键盘全流程操作、localStorage 存档、静态部署到任意静态托管

## 适用场景

- 零基础者通过游戏化的碎片拼组方式入门提示工程
- 课堂或离线环境中自学提示技术并核对官方出处
- 系统化梳理各家厂商（OpenAI/Anthropic/Google 等）提示技巧差异

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L25: Each of the **130 teaching shrines covers exactly one skill**, taken from **official vendor documentation** — OpenA
> L27: in-game and 370 of them deep-linked straight to the paragraph being quoted). Scoring runs **entirely offline** — no
> L173: - **The core loop never calls a model.** Everything above runs in the browser, from data in the repo.

## 星数曲线

```mermaid
xychart-beta
    title "romanticamaj/promptasy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-25 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `5162cd72fe68` · [字段定义](../../DATASET.md)*
