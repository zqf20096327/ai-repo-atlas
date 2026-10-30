# joshspeagle/aparture

⭐ 20 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/joshspeagle/aparture) · [官网](https://joshspeagle.com/aparture/) · 个人维护

**按研究者兴趣自动筛选 arXiv 论文并生成日报的工具**

研究者用自然语言描述研究方向，每次运行将当日 arXiv 论文与描述匹配，全文阅读最相关论文，生成一篇串联多篇论文的简报；每条引用在渲染前会对照原论文核查，用户可反馈误判并接受或拒绝对研究画像的修改。程序在本地运行，使用用户自己的 API key。安装方式为 git clone 源码加 npm，通过 Next.js 开发服务器在 localhost 使用。作者为天文/统计方向研究者，工作流以研究者需求为先。

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

- 按自然语言研究描述过滤当日 arXiv 论文并全文阅读
- 生成一篇串联多篇论文的简报，引用渲染前逐条核查
- 误判反馈机制：接受或拒绝对研究画像的修改
- 本地运行，使用用户自己的 API key

## 适用场景

- 每日跟踪 arXiv 上与自身研究相关的论文，替代手动刷列表
- 获得一篇将多篇相关论文串联起来的简报
- 通过反馈逐步校正论文筛选的匹配画像

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L5: Aparture exists so a researcher can stop skimming the arXiv without worrying about what they're missing. You describ
> L38: **Note:** Originally built to help the author (Josh Speagle) manage daily paper monitoring across cs, stat, and ast

## 星数曲线

```mermaid
xychart-beta
    title "joshspeagle/aparture 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `68e2c94ba927` · [字段定义](../../DATASET.md)*
