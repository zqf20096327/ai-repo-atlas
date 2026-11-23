# mujakayadan/Resume-Builder-TeX

⭐ 10 · Python · MIT · 推送 2026-08-23 · [GitHub](https://github.com/mujakayadan/Resume-Builder-TeX) · 个人维护

**求职者：用 LLM 从职位描述生成定制简历与求职信**

读取职位描述与个人信息 JSON，调用 OpenAI 与 Anthropic 的语言模型为简历和求职信各小节生成针对性内容，套用 LaTeX 模板编译为 PDF，并按公司/职位自动归档到独立文件夹。支持从 Indeed 抓取解析职位描述；LaTeX 模板存于数据库，通过 DatabaseManager 读取更新。依赖系统安装 LaTeX；该仓库已停止维护，由 YARBA 接替。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 调用 OpenAI/Anthropic API 按职位描述逐节生成简历与求职信内容
- LaTeX 模板编译输出 PDF，按公司职位自动归档
- 支持解析 Indeed 职位描述页面
- 提供 Docker 部署方式

## 适用场景

- 针对每个职位描述快速生成定制化简历和求职信
- 批量管理不同公司申请用的简历文件
- 从 Indeed 职位页面直接导入职位描述

## 场景标签

`AI 写作` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L23: The AI-Powered Resume and Cover Letter Generator is a sophisticated tool designed to automate the creation of profe
> L27: - **AI-Driven Content Generation**: Utilizes AI to analyze job descriptions and generate customized resume and cove

## 星数曲线

```mermaid
xychart-beta
    title "mujakayadan/Resume-Builder-TeX 星数(近 2 点)"
    x-axis ["2026-10-20", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-20 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `3fcf5abe85a7` · [字段定义](../../DATASET.md)*
