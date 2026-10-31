# NC0DER/KeyphraseExtraction

⭐ 14 · Python · GPL-3.0 · 推送 2025-12-17 · [GitHub](https://github.com/NC0DER/KeyphraseExtraction) · 个人维护

**关键词/关键短语抽取方法的文献综述与对比评估代码集**

配套两篇论文（关键词与关键短语抽取的文献综述、多语言无监督关键短语抽取方法的对比评估）的代码仓库：收录被评估各方法的代码，作者对其做了适配修改（去除硬编码路径、对显存需求高的方法设置 cpu-only、Python 2 转 Python 3、修正旧包报错、统一 stemming 时机），并统一跑测试。数据集以外部链接提供，安装需按各子目录说明分别进行，配置 KeyExt/config.py 后运行 KeyExt.py 复现结果。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 收录多篇论文中被评估的关键短语抽取方法代码
- 对原始代码做了 cpu-only、Python 3 迁移等适配修改
- 通过 KeyExt.py 统一运行并输出测试结果

## 适用场景

- 复现论文中的关键短语抽取方法对比评估
- 在统一环境下运行多种抽取方法并比较结果
- 获取关键短语抽取文献综述的配套代码与数据集入口

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: This repository hosts code for the papers:
> L4: * A literature review of keyword and keyphrase extraction - - Download
> L22: ## Test Results

## 星数曲线

```mermaid
xychart-beta
    title "NC0DER/KeyphraseExtraction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `466d20e50e46` · [字段定义](../../DATASET.md)*
