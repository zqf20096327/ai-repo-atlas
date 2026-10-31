# Armaan29-09-2005/AI-OSINT-Security-Analyzer

⭐ 14 · Python · MIT · 推送 2026-10-12 · [GitHub](https://github.com/Armaan29-09-2005/AI-OSINT-Security-Analyzer) · 个人维护

**面向安全分析者的 AI 驱动 OSINT 威胁评估 Web 应用**

基于 Streamlit 的 Python Web 应用，面向需要安全评估的用户：输入网站 URL、IP 地址或 CVE ID，应用聚合 Shodan、VirusTotal、AbuseIPDB 与 CVE 数据库的多源数据，并调用 Cohere Command A 模型生成自然语言的威胁评估结果。安装方式为克隆仓库、pip 安装依赖后以 streamlit run 启动，本地浏览器访问 localhost:8501；另有 GitHub Releases 提供可下载版本。需自行准备所查询数据源的访问条件（README 未列出 API key 配置细节）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持网站、IP 地址、CVE 与软件漏洞的综合威胁分析
- 集成 Shodan / VirusTotal / AbuseIPDB / CVE 多源数据
- 使用 Cohere Command A 模型生成 AI 分析
- Streamlit Web 界面，可自定义选择查询的数据源

## 适用场景

- 我想快速评估一个网站或 IP 的威胁状况
- 我想查询某个 CVE 的相关信息并得到 AI 汇总分析
- 我想聚合多个威胁情报源做一次性安全检查

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L5: Welcome to the **AI OSINT Security Analyzer**! This project leverages cutting-edge AI technology to enhance cybersec
> L12: - **AI-Driven Insights**: Utilize Cohere's Command A model for enhanced analysis.
> L55: 3. **Run Analysis**: Click the "Analyze" button to begin the assessment.

## 星数曲线

```mermaid
xychart-beta
    title "Armaan29-09-2005/AI-OSINT-Security-Analyzer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `12a56fde0c9c` · [字段定义](../../DATASET.md)*
