# antononcube/Raku-WWW-OpenAI

⭐ 10 · Raku · Artistic-2.0 · 推送 2026-11-16 · [GitHub](https://github.com/antononcube/Raku-WWW-OpenAI) · [官网](https://raku.land/zef:antononcube/WWW::OpenAI) · 个人维护

**Raku 语言的 OpenAI API 访问库，封装文本/图像/音频/嵌入接口**

面向 Raku 开发者的 OpenAI API 客户端包，通过 zef 安装。提供统一入口函数 openai-playground 及分类函数：文本生成（Responses 与 Chat Completions 路径）、图像生成/变体/编辑、视觉描述、内容审核、音频转录与翻译、语音合成、嵌入向量。API key 可经 OPENAI_API_KEY 环境变量注入；模型 ID 内置现用与遗留清单，遗留 ID 在 OpenAI 仍服务期间可选。作者声明其功能范围小于 OpenAI 官方 Python 包，代码按功能拆分为独立文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | Artistic-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 统一前端函数 openai-playground 覆盖多种 OpenAI 功能
- 支持文本生成、图像生成/编辑、视觉、审核、音频转录翻译、语音合成、嵌入
- API key 支持通过 OPENAI_API_KEY 环境变量读取
- 内置现用与遗留模型 ID 清单，可用 openai-models 查询账户可用模型

## 适用场景

- 在 Raku 项目中调用 OpenAI 生成文本与代码
- 用 Raku 脚本批量生成或编辑图像
- 对音频文件做转录与翻译
- 获取文本嵌入向量并做相似度分析

## 场景标签

 · 领域:LLM 基础设施/API 客户端

## 证据(README 行号)

> L5: This Raku package provides access to the machine learning service OpenAI, [OAI1].
> L42: The package has an universal "front-end" function `openai-playground` for the

## 星数曲线

```mermaid
xychart-beta
    title "antononcube/Raku-WWW-OpenAI 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `06aeea638bb4` · [字段定义](../../DATASET.md)*
