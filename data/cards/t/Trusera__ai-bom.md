# Trusera/ai-bom

⭐ 346 · Python · Apache-2.0 · 推送 2026-05-24 · [GitHub](https://github.com/Trusera/ai-bom) · [官网](https://trusera.dev) · 组织维护

**扫描代码库发现 AI 组件并生成合规 AI-BOM 的 CLI 工具**

Python CLI 工具 ai-bom：通过 13 个自动注册的扫描器分析源码、Docker/K8s、网络环境、云 IaC、n8n 工作流、Jupyter、MCP 配置、GitHub Actions 与模型文件，识别项目中的 AI agent、模型与 API 集成，输出带 0-100 风险评分的组件清单；支持 CycloneDX 1.6、SARIF、SPDX 3.0、HTML 仪表盘等 9 种输出格式，并对照 EU AI Act、OWASP、许可证做合规检查。面向需要满足 EU AI Article 53 组件清单要求或审计 Shadow AI 的开发与安全团队。提供 pip/pipx 安装、Docker 镜像、GitHub Action、GitLab CI 模板与 VS Code 扩展；可选安装 callable 扩展将发现的组件转为可调用模型，另有 Trusera SDK 拦截器与 Cedar 策略门控作为配套组件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 13 个扫描器覆盖源码、IaC、n8n、MCP 配置、模型文件等输入
- 0-100 风险评分与 EU AI Act / OWASP / 许可证合规模块
- 9 种输出格式（CycloneDX/SARIF/SPDX/HTML/Markdown 等）
- GitHub Action、GitLab CI 模板、VS Code 扩展与策略门控（YAML/Cedar）

## 适用场景

- 为 EU AI Act 合规生成 AI 组件清单（AI-BOM/SBOM）
- 在 CI 中扫描新增 AI/LLM 集成并按严重度阻断
- 审计 n8n 工作流与 MCP 配置中的危险组合与硬编码凭据

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L27: **EU AI Act (Article 53, Aug 2025)** requires a complete AI component inventory — no existing SBOM tool covers AI.
> L187:  S[Scanner Engine 13 Auto-Registered Scanners] --> M[Pydantic Models AIComponent + ScanResult]

## 星数曲线

```mermaid
xychart-beta
    title "Trusera/ai-bom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 345 --> 347
    line [346, 346]
```

2026-10-18 346 → 2026-10-22 346（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `e9a626dbbb47` · [字段定义](../../DATASET.md)*
