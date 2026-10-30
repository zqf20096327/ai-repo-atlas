# Sathvik-Rao/StackResume

⭐ 16 · Python · GPL-3.0 · 推送 2026-06-09 · [GitHub](https://github.com/Sathvik-Rao/StackResume) · [官网](https://hub.docker.com/r/sathvikrao/stackresume) · 个人维护

**自托管 AI 简历生成器：一句话输入产出 ATS 优化简历**

面向软件开发者的自托管开源简历生成工具：以聊天式 Web UI 为入口，九个 LangGraph 编排的 agent 完成输入解析、简历 JSON 生成（STAR 格式量化要点）、Reviewer→Enhancer 质量循环评分与改写，可选按职位描述定制求职信与外联邮件模板，导出 PDF/Word/ODT 五种模板。支持 OpenAI、Anthropic、Google Gemini、Ollama 本地推理及 OpenAI 兼容端点，数据存于单文件 SQLite，Docker 单容器部署，GPL-3.0 许可，可开启单用户认证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 九 agent 流水线含 Reviewer→Enhancer 质量循环（阈值 82 分，最多 3 轮）
- 按 JD 定制强度滑块（0-100）并生成求职信与 2-4 类外联模板
- 多提供商支持：OpenAI/Anthropic/Gemini/Ollama（本地离线）/自定义 OpenAI 兼容端点
- 数据存单文件 SQLite，导出 PDF/Word/ODT 五种模板，含应用追踪器与主简历对比

## 适用场景

- 软件开发者用一句话生成可导出的 ATS 优化简历
- 粘贴职位描述后定制简历、求职信与外联邮件
- 在自有设备上离线（Ollama）生成简历，数据不出本机

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L24: StackResume turns minimal input into a polished, interview-ready software-developer resume. The multi-agent pipelin
> L28: - **Reviews & enhances** in a loop — a Reviewer agent scores ATS compatibility, writing quality, impact, and comple
> L111: Nine specialised agents orchestrated with LangGraph — each resume goes through intent guarding, input parsing, opt

## 星数曲线

```mermaid
xychart-beta
    title "Sathvik-Rao/StackResume 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `69b4b1059d41` · [字段定义](../../DATASET.md)*
