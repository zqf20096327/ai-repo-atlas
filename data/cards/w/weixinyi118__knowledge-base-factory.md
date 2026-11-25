# weixinyi118/knowledge-base-factory

⭐ 3 · Python · MIT · 推送 2026-10-29 · [GitHub](https://github.com/weixinyi118/knowledge-base-factory) · 个人维护 · 中文 README

**3 秒生成知识库骨架 CLI，配套写作标准与体检脚本**

一个 Python CLI 工具，按预设分类（opc/content/tech）3 秒生成 Markdown 知识库目录骨架：总目录、分类索引、元数据八字段规范、写作标准与验收单。核心机制是模板+写作标准+体检脚本：check.py 提供 13 项分级检查（断链、companion 空引用、索引漏篇、禁用词等），支持 --fix 自动修复与 --json 输出，P0 错误返回退出码可挂 CI。纯标准库实现，Python 3.8+ 即可运行，生成时将工具复制进库内自检。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 3 秒生成含总目录、分类索引、元数据规范的知识库骨架
- 13 项分级体检脚本（P0/P1/P2），支持 --fix 自动修复与 --json 输出
- 内置去 AI 味写作标准：证据挂靠、禁用词替换表、开场方式轮换
- P0 错误返回退出码 1，可直接挂 CI

## 适用场景

- 给 APP、社群或内部团队做几十到几百篇的可检索内容库
- 把散落的笔记、收藏、草稿整理成有分类有索引的体系
- 内容团队建立统一的写作与验收标准
- 在 Obsidian 里快速建库而不必每次重新设计目录结构

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L18: 所以这套东西的核心不是模板，是**模板 + 标准 + 会抓错的脚本**。三样缺一样都不成立。
> L43: 纯标准库，无依赖，Python 3.8+。Windows / macOS / Linux 都行。
> L64: **库自带体检工具。** 生成时把 `check.py` 和 `export.py` 复制进 `tools/`，clone 下来就能查，不用回头找这个仓库。

## 星数曲线

```mermaid
xychart-beta
    title "weixinyi118/knowledge-base-factory 星数(近 2 点)"
    x-axis ["2026-10-31", "2026-11-25"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-31 3 → 2026-11-25 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `fd621f854eab` · [字段定义](../../DATASET.md)*
