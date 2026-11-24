# noviqtechnologies/vexa-sca

⭐ 6 · Rust · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/noviqtechnologies/vexa-sca) · 组织维护

**给 DevSecOps 团队的软件成分分析与漏洞扫描引擎**

以 Rust 编写的软件成分分析（SCA）与安全引擎：解析多语言 manifest 与 lockfile 构建传递依赖图，结合 OSV/CISA KEV/EPSS 数据做漏洞分诊，并提供 AST 用法信号区分已引用与未引用依赖。附加能力包括 PR 差异扫描、同主版本优先的修复建议、CycloneDX/SPDX SBOM 导出、SAST 与密钥检测、npm/pip 等安装前防火墙，以及向 AI 编码助手暴露 4 个工具的 MCP 服务器。支持本地二进制、npm 启动器、Docker 与 GitHub Actions 运行；Vexa Cloud 免费额度为每月 500 次扫描。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 单二进制、多线程扫描，零外部 C/OpenSSL 运行时依赖
- CycloneDX v1.5（含 VEX）与 SPDX v2.3 SBOM 导出，SARIF v2.1.0 输出
- EPSS 利用预测与 CISA KEV 目录集成的漏洞优先级排序
- MCP 服务器向 Cursor/Claude Code 等 AI 编码助手暴露 4 个工具

## 适用场景

- 在 CI/CD 与 PR 流程中拦截新引入的漏洞
- 为交付物生成合规的 SBOM 报告
- 在安装依赖前用 wrap 阻断 typosquatting 与已知被利用包
- 离线/隔离环境下用签名 .vexadb 离线数据库扫描

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L15: **Vexa SCA** (`vexa-sca`) is an open-source, high-performance Software Composition Analysis (SCA) engine built in R
> L46: |🤖 **MCP Server (`mcp`)**|JSON-RPC 2.0 MCP server exposing 4 tools to AI coding assistants (Cursor, Claude Code, Wi

## 星数曲线

```mermaid
xychart-beta
    title "noviqtechnologies/vexa-sca 星数(近 3 点)"
    x-axis ["2026-10-30", "2026-10-31", "2026-11-24"]
    y-axis "stars" 4 --> 7
    line [5, 6, 6]
```

2026-10-30 5 → 2026-11-24 6（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `8eacfee2d428` · [字段定义](../../DATASET.md)*
