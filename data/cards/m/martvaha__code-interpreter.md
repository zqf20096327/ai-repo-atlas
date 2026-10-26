# martvaha/code-interpreter

⭐ 37 · Python · 推送 2026-06-12 · [GitHub](https://github.com/martvaha/code-interpreter) · 个人维护

**兼容 LibreChat 规范的代码解释器服务，Docker 沙箱执行代码**

基于 FastAPI 的代码执行与文件管理服务，实现 LibreChat Code Interpreter API 规范，供 LibreChat 部署自托管代码解释器使用。代码在隔离的 Docker 容器沙箱中执行，支持自定义镜像、文件上传下载、并发执行，语言支持 Python 与 R。通过 LibreChat 签发的短期 JWT（EdDSA/Ed25519，亦支持 RS256）鉴权，未配置公钥时默认无鉴权。README 声明本项目主要为概念验证，不建议用于生产环境。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 单 docker compose 文件部署，代码在隔离 Docker 沙箱中执行（支持自定义镜像）
- 兼容 LibreChat Code Interpreter API 规范，JWT（EdDSA/RS256）鉴权
- 支持文件上传下载、并发执行、Python 与 R 语言
- RESTful API 附 OpenAPI 文档

## 适用场景

- 为 LibreChat 部署自托管的代码解释器后端
- 在隔离沙箱中执行 Python/R 代码并管理上传文件
- 开发测试场景下快速起一个兼容 LibreChat 规范的代码执行服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: A FastAPI-based code interpreter service that provides code execution and file management capabilities. This service
> L6: > This project is mostly a proof of concept and is not intended to be used in production.
> L13: - Code is executed in a isolated Docker container sandbox, custom images supported

## 星数曲线

```mermaid
xychart-beta
    title "martvaha/code-interpreter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `aed8bf60f0d6` · [字段定义](../../DATASET.md)*
