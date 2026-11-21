# engrshoaibh/owasp-security-audit-skill

⭐ 4 · Python · NOASSERTION · 推送 2026-11-18 · [GitHub](https://github.com/engrshoaibh/owasp-security-audit-skill) · 个人维护

**供 AI 编码代理执行的 OWASP 安全审计技能与漏洞扫描工具集**

面向 AI 编码代理（Claude Code、Cursor、Windsurf 等）的安全审计技能，同时附带可独立运行的 Python 自动化脚本。核心机制：通过 manifest 自动检测项目技术栈，按渐进式披露仅加载相关检查清单以节省上下文；编排 Gitleaks、Semgrep、Trivy、Checkov 等扫描器，自动管理无头 OWASP ZAP 进程生命周期，输出六步审计流程（含 SCA、DAST、修复登记表）。核心工具仅需 Python 3.10+，运行 ZAP 需 Java。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 渐进式披露机制按项目栈自动裁剪加载的检查清单
- 自动管理无头 ZAP 守护进程的启动、扫描与清理
- 多工具编排：Gitleaks、Semgrep、Trivy、OSV-Scanner、Checkov 等
- 内置纯标准库静态扫描器检测硬编码密钥、注入点与资源耗尽循环

## 适用场景

- 让 AI 编码代理对代码仓库执行 OWASP 对齐的安全审计
- 检测项目中的泄露密钥、依赖漏洞与基础设施即代码配置问题
- 对本地或预发布环境的 Web/API 端点运行 DAST 扫描

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: > **Comprehensive, token-efficient security audit skill and automated loophole scanner for AI coding agents, develop
> L24: The **OWASP Security Audit Skill** resolves both issues. It acts as an intelligent, progressive-disclosure skill fo
> L31: - **Built-in Static Loophole & Resource Exhaustion Scanner:** Standard-library scanner detecting hardcoded secrets,

## 星数曲线

```mermaid
xychart-beta
    title "engrshoaibh/owasp-security-audit-skill 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-21"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-11-18 4 → 2026-11-21 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `5d40c79735f7` · [字段定义](../../DATASET.md)*
