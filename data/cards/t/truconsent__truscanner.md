# truconsent/truscanner

⭐ 18 · Python · MIT · 推送 2026-07-06 · [GitHub](https://github.com/truconsent/truscanner) · [官网](https://truconsent.io) · 组织维护

**扫描源码发现个人数据元素与隐私数据流的静态分析工具**

面向开发者与安全团队的静态代码分析 CLI/Python 库：加载 data_elements/ 目录下的全量数据元素定义（示例 380 条，覆盖 300+ 种 PII、金融数据、设备标识符等），用正则扫描源码目录并生成 TXT/Markdown/JSON 报告，含扫描 ID、token 用量、按文件与类别的汇总。AI 为可选增强路径：正则扫描与 AI 扫描分离运行，可选 Ollama/OpenAI/AWS Bedrock/Google Vertex AI 提供方，支持 fast/balanced/full 三档模式。可选上传报告至 app.truconsent.io 后端。Python 3.9+，pip 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 加载全量数据元素目录进行正则扫描（非截断子集）
- 正则扫描与 AI 扫描为两条独立路径，AI 提供方可选 Ollama/OpenAI/Bedrock/Vertex
- 生成 TXT/Markdown/JSON 报告，含 token 用量统计与自动递增命名
- 报告可选择性上传至后端 API 集中查看

## 适用场景

- 在代码库中定位 PII 等个人数据元素以满足 DPDP 等隐私合规要求
- 安全团队对项目源码做隐私数据流盘点并留存报告
- 用本地 Ollama 模型做离线的 AI 增强扫描

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: `truScanner` is a static code analysis tool designed to discover and analyze personal data elements in your source c
> L18: - **Separate Regex and AI Scans**: Regex/static scanning and AI-enhanced scanning now run as distinct paths
> L19: - **AI-Powered Enhancement**: Optional integration with Ollama, OpenAI, AWS Bedrock, or Google Vertex AI for deeper

## 星数曲线

```mermaid
xychart-beta
    title "truconsent/truscanner 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `843b237a6365` · [字段定义](../../DATASET.md)*
