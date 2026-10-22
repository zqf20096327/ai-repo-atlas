# lmstudio-ai/lmstudio-python

⭐ 885 · Python · MIT · 推送 2025-10-27 · [GitHub](https://github.com/lmstudio-ai/lmstudio-python) · [官网](https://lmstudio.ai/docs/python) · 组织维护

**面向开发者的 LM Studio Python SDK：接入本地 LLM**

由 lmstudio-ai 维护的官方 Python SDK，通过 websocket 连接 LM Studio 实例，提供同步 Client 与顶层便捷 API，可请求文本补全与带聊天历史的对话响应；模型 API 由 lmstudio-js schema 自动生成。安装支持 PyPI 与源码克隆两种方式。开发流程采用 pdm/tox，配套 ruff 格式化、mypy 严格模式类型检查与 pytest 多版本测试。版本采用类语义化的 X.Y.Z 三段编号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同步 Client 管理 websocket 连接，另有隐式默认实例的顶层便捷 API
- 数行代码即可请求已加载 LLM 的补全或聊天响应
- API 模型由 lmstudio-js schema 脚本自动生成
- 开发流程含 ruff/mypy/pytest/tox 多版本测试

## 适用场景

- 在 Python 程序中调用 LM Studio 已加载的本地模型
- 为本地 LLM 应用构建对话式接口
- 参与 SDK 开发与贡献

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L1: # LM Studio Python SDK
> L18: The base component of the LM Studio SDK is the (synchronous) `Client`.
> L20: websocket connections to the LM Studio instance.

## 星数曲线

```mermaid
xychart-beta
    title "lmstudio-ai/lmstudio-python 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-21"]
    y-axis "stars" 881 --> 885
    line [882, 884, 884]
```

2026-10-18 882 → 2026-10-21 884（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1687720d3715` · [字段定义](../../DATASET.md)*
