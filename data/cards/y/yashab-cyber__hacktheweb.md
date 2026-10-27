# yashab-cyber/hacktheweb

⭐ 41 · Python · MIT · 推送 2026-07-04 · [GitHub](https://github.com/yashab-cyber/hacktheweb) · [官网](https://yashab-cyber.github.io/hacktheweb/) · 个人维护

**面向安全专业人员的 Web 应用渗透测试工具，含规则式 AI 扫描**

基于 Python 的命令行 Web 应用渗透测试工具，面向安全专业人员与道德黑客，覆盖 XSS、SQL 注入、CSRF、SSRF、LFI/RFI、XXE、RCE、IDOR、SSTI 等 15 类漏洞检测。其 AI 部分为纯规则引擎（无外部 ML 模型依赖），提供自适应扫描策略、技术栈识别与指纹识别；支持 HTML/PDF/JSON/Markdown 报告与 OWASP/CWE 映射，内置 500+ payload 可通过 data/ 目录自定义。要求 Linux 环境（Kali/Ubuntu/Debian）与 Python 3.8+，提供 Python API，Docker 安装标注 Coming Soon。仅限授权安全测试使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 15 类漏洞扫描（XSS/SQLi/CSRF/SSRF/RCE/SSTI 等）
- 规则式 AI 引擎，无需外部 ML 模型，自适应扫描策略
- HTML/PDF/JSON/Markdown 报告与 OWASP/CWE 映射
- 内置 500+ payload 数据库，可自定义扩展

## 适用场景

- 对已授权的 Web 应用做自动化渗透测试
- 生成带严重性分级与修复建议的安全报告
- 输出结构化 JSON 日志接入 Splunk/ELK 等 SIEM

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L16: **HackTheWeb** is a production-ready, AI-powered web application penetration testing tool designed for security pro
> L22: - **🔧 No ML Models:** Pure rule-based AI - no external dependencies

## 星数曲线

```mermaid
xychart-beta
    title "yashab-cyber/hacktheweb 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-27 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `7be57ab0db5a` · [字段定义](../../DATASET.md)*
