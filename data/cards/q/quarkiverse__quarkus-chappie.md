# quarkiverse/quarkus-chappie

⭐ 16 · JavaScript · Apache-2.0 · 推送 2026-10-08 · [GitHub](https://github.com/quarkiverse/quarkus-chappie) · [官网](https://docs.quarkiverse.io/quarkus-chappie/dev/) · 组织维护

**Quarkus Dev Mode 的 AI 助手扩展，辅助开发排错**

Quarkus 生态的 Dev Mode 专用扩展：为开发者提供 AI 辅助，包括异常界面的 AI 协助与基于 RAG 的文档检索问答。需配置 OpenAI 兼容服务或本地 Ollama；1.7.x 起文档检索数据从 Maven Central 自动加载，旧版本回退到预构建 chappie-ingestion-quarkus 镜像。仅作用于开发模式，不进入生产应用。2.x 面向 Quarkus 4 且要求 JDK 21，Quarkus 3 用户使用 1.7.x 分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Dev Mode 专用扩展，不影响生产应用
- 支持 OpenAI 兼容服务或本地 Ollama 配置
- 1.7.x 起文档检索数据从 Maven Central 自动加载
- Windows 下 RAG 需安装 VC++ Redistributable（ONNX Runtime/BGE embedding）

## 适用场景

- 开发 Quarkus 应用时在异常界面获得 AI 协助
- 在 Dev Mode 中查询框架文档得到带出处的回答
- 本地 Ollama 环境下离线使用 AI 开发辅助

## 场景标签

`AI 助手` `文档问答` · 领域:对话与助手

## 证据(README 行号)

> L7: This extension adds some AI to you quarkus dev experience. To use this in your project, simply add the
> L29: To use chappie, you need to configure it with either an OpenAI Compatible Service or have Ollama running locally. Y

## 星数曲线

```mermaid
xychart-beta
    title "quarkiverse/quarkus-chappie 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `453c9f71e39b` · [字段定义](../../DATASET.md)*
