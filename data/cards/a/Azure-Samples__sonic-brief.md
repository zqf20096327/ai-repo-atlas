# Azure-Samples/sonic-brief

⭐ 37 · TypeScript · 推送 2026-04-11 · [GitHub](https://github.com/Azure-Samples/sonic-brief) · 组织维护

**Azure 上的语音转写与摘要报告生成系统**

基于 Azure 云服务的音频处理解决方案加速器：用户经 React Web 界面上传录音，Azure Speech-to-Text 转写文本，Azure OpenAI GPT-4o 按可自定义的提示词生成结构化摘要报告，结果存于 Blob Storage 并可用 CosmosDB 记录元数据与日志。面向企业、医疗、法律等需批量处理录音的组织，需 Microsoft Azure 账户及多项 Azure 服务，支持手动部署与 Terraform 自动部署。README 声明项目处于早期阶段，可能发生变化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Azure Speech-to-Text 转写 + GPT-4o 摘要的端到端异步工作流
- 用户可自定义摘要提示词并查看/下载转录与 PDF 报告
- 支持 Azure Portal 手动部署与 Terraform 自动部署两种方式
- 内置医疗问诊、社工面谈、呼叫中心 QA、法律文档等用例场景

## 适用场景

- 医院将医患对话转为结构化病历记录
- 呼叫中心对客服录音做摘要与质检报告
- 律所将会议与法律程序录音转为可检索文档

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L10: Azure Voice Notes is a cloud-based audio processing system that allows users to efficiently process voice recording
> L63: 6. **Azure OpenAI GPT-4o** - Summarizes the transcribed text.

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/sonic-brief 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-31 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cdf771614df4` · [字段定义](../../DATASET.md)*
