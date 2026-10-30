# langchain-ai/langsmith-java

⭐ 34 · Kotlin · MIT · 推送 2026-10-29 · [GitHub](https://github.com/langchain-ai/langsmith-java) · 组织维护

**LangSmith 平台的 Java SDK：供 Java 应用访问其 REST API**

由 langchain-ai 维护的 LangSmith Java SDK，封装 LangSmith REST API 的访问：提供同步与异步客户端、运行查询、文件上传（Path/InputStream/byte[]）、自动与手动分页、原始响应访问、按 HTTP 状态码分类的异常体系、默认 2 次指数退避重试与 90 秒超时。客户端经系统属性或环境变量（LANGSMITH_API_KEY/LANGSMITH_ENDPOINT 等）配置。要求 Java 8 及以上，依赖 Jackson（默认 2.22.0，兼容 2.13.4+），发布于 Maven Central 并带示例模块。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步/异步客户端，异步方法返回 CompletableFuture
- SandboxClient 操作自动附加 sandbox_id 追踪元数据
- 文件上传支持 Path/InputStream/byte[]/MultipartField
- 与 ProGuard/R8 兼容（发布 keep rules），Jackson 版本运行时校验

## 适用场景

- 在 Java 服务中接入 LangSmith 进行 LLM 运行追踪与查询
- 从 Java 应用上传数据集文件到 LangSmith
- Android（R8/ProGuard）项目中使用 LangSmith SDK

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L6: The LangSmith Java SDK provides convenient access to the LangSmith REST API from applications written in Java.
> L71: Operations through `SandboxClient` and its `Sandbox` handles add `sandbox_id` to the active

## 星数曲线

```mermaid
xychart-beta
    title "langchain-ai/langsmith-java 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-30"]
    y-axis "stars" 32 --> 35
    line [33, 34, 34]
```

2026-10-18 33 → 2026-10-30 34（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7e7fe32c73b4` · [字段定义](../../DATASET.md)*
