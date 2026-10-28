# Humor-Research/KoWit-24

⭐ 22 · Jupyter Notebook · 推送 2026-05-02 · [GitHub](https://github.com/Humor-Research/KoWit-24) · 组织维护

**俄语新闻标题文字游戏细粒度标注数据集（2,700 条）**

KoWit-24 是对 2,700 条俄语新闻标题做人工细粒度标注的双语戏谑数据集：1,340 条含文字游戏，标注内容包括是否存在文字游戏、类型（双关/变形/新造词/矛盾修饰等）、锚点子串、所指字符串及 Wikipedia/Wiktionary 链接；每条标题附新闻导语与摘要作为上下文。数据集可从本仓库或 Hugging Face 下载，附五个 LLM（GPT-4o、GigaChat、YandexGPT4 等）在检测与解释任务上的实验结果，并提供可 pip 安装的自动评估函数与 LangChain Hub 提示词。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 2,700 条人工标注标题，正负类近均衡（1,340 含文字游戏）
- 标注含锚点子串、所指字符串与 Wikipedia/Wiktionary 链接
- 每条标题附新闻导语与摘要作为上下文
- 提供 pip 安装的自动解释评估函数与五个 LLM 的实验结果

## 适用场景

- 评测 LLM 对文字游戏的检测与解释能力
- 研究俄语新闻标题中的双关与习语变形现象
- 训练或测试幽默/文字游戏分类模型

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L11: We present KoWit-24, a dataset with fine-grained annotation of wordplay in 2,700 Russian news headlines. KoWit-24 a
> L43: Unlike the majority of existing humor collections of canned jokes, KoWit-24 provides wordplay contexts – each headl

## 星数曲线

```mermaid
xychart-beta
    title "Humor-Research/KoWit-24 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `0a58a2ca3767` · [字段定义](../../DATASET.md)*
