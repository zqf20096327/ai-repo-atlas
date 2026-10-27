# IAAR-Shanghai/SurveyX

⭐ 995 · TeX · 推送 2026-01-12 · [GitHub](https://github.com/IAAR-Shanghai/SurveyX) · [官网](http://www.surveyx.cn) · 组织维护 · 中文 README

**给科研人员：输入标题与关键词，基于本地文献生成学术综述**

SurveyX 是利用 LLM 生成特定领域学术综述论文的系统。开源离线版流程：用户将参考文献转为 Markdown 放入单一目录，配置自有 LLM API（OpenAI 兼容接口与嵌入模型 API），运行 pipeline 依次生成大纲、正文、精修与 LaTeX 源码，经本地 texlive 编译输出 survey.pdf。限制：开源版不含在线检索、关键词扩展、语义过滤与多模态解析，完整功能需登录官网（由 MemTensor 上海公司托管），生成的论文仍需人工核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 输入标题+关键词+本地 Markdown 文献，自动生成大纲、正文与 LaTeX 综述
- 分步工作流：outline→content→post refine→LaTeX 生成，结果按 task_id 归档
- LLM 接口可配置（OpenAI 兼容 API + 独立嵌入模型 API）
- 开源版为离线简化版，完整版通过官网使用

## 适用场景

- 我有了一批文献 Markdown，想快速产出某主题的综述初稿
- 科研写作中生成结构化大纲与 LaTeX 源码
- 体验 SurveyX 论文方法对应的离线实现

## 场景标签

`科研工具` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L34: **SurveyX** is an advanced academic survey automation system that leverages the power of Large Language Models (LLM
> L89: python tasks/offline_run.py --title "Your Survey Title" --key_words "keyword1, keyword2, ..." --ref_path "path/to/y

## 星数曲线

```mermaid
xychart-beta
    title "IAAR-Shanghai/SurveyX 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 993 --> 996
    line [994, 995, 995]
```

2026-10-18 994 → 2026-10-27 995（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `af1ca98530eb` · [字段定义](../../DATASET.md)*
