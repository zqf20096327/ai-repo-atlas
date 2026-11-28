# epam/ai-dial-core

⭐ 662 · Java · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/epam/ai-dial-core) · [官网](https://dialx.ai) · 组织维护

**AI DIAL 核心组件：为模型与应用提供统一 API**

DIAL Core 是 AI DIAL 平台的主组件，以 HTTP 代理形式为不同聊天补全与嵌入模型、助手和应用提供统一 API。基于 Java 25 与 Eclipse Vert.x 实现，自动生成 OpenAPI 3.0 规范描述全部 REST 端点。支持 Gradle 构建与运行，可经 Helm chart 部署到 Kubernetes（含完整平台 umbrella chart 或仅 Core 两种方式）。配置分静态（启动时生效，环境变量/文件/默认资源三级优先级）与动态两类，并提供插件加载、分析日志、OTel 追踪等运行时设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 API 代理聊天补全与嵌入模型、助手和应用
- 自动生成 OpenAPI 3.0 规范（docs/open_api_core.yaml）
- 静态/动态两级配置与启动时插件目录加载机制
- 支持 Helm 单组件部署或 DIAL 平台 umbrella chart 部署

## 适用场景

- 为多个聊天补全与嵌入模型提供统一 API 入口
- 在 Kubernetes 集群上部署 DIAL 平台核心组件
- 集中管理 API key、角色共享与请求分析日志

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: > HTTP Proxy provides unified API to different chat completion and embedding models and applications.
> L82: You have the option to deploy the DIAL Core on the Kubernetes cluster by utilizing an _umbrella_ dial Helm chart, w

## 星数曲线

```mermaid
xychart-beta
    title "epam/ai-dial-core 星数(近 6 点)"
    x-axis ["2026-10-26", "2026-10-30", "2026-11-06", "2026-11-08", "2026-11-26", "2026-11-28"]
    y-axis "stars" 660 --> 664
    line [661, 662, 661, 663, 662, 662]
```

2026-10-26 661 → 2026-11-28 662（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `15ead7aca536` · [字段定义](../../DATASET.md)*
