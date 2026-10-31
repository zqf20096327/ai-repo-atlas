# JADBio/JADBioPythonClient

⭐ 15 · Python · GPL-3.0 · 推送 2026-06-02 · [GitHub](https://github.com/JADBio/JADBioPythonClient) · 组织维护

**JADBio AutoML 平台的 Python API 客户端**

由 JADBio 公司维护的 Python 客户端 JADExpert，通过 HTTP GET/POST 调用把 JADBio AutoML 平台的主要功能开放给 Python 用户：POST 用于资源创建、修改、删除，GET 为只读幂等操作。平台面向生命科学专业人员，提供建模与部署能力。安装途径含源码 pip install .、PyPI 与 Anaconda 频道，支持 Sphinx 生成文档并附带示例代码与示例数据集。注意 1.2.12 及以下版本因 API URL 变更不可用，需升级或显式指定 host。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 HTTP GET/POST 封装 JADBio 平台主要功能
- 支持 PyPI、Anaconda 与源码三种安装方式
- 提供 src/examples 示例代码与示例数据集
- 支持 Sphinx 本地生成文档

## 适用场景

- 在 Python 中调用 JADBio 平台完成建模任务
- 脚本化创建、读取、删除平台上的资源
- 用示例数据集试用客户端功能

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L18: JADBio's purpose-built AutoML platform provides leading-edge AI tools and automation capabilities enabling life-sci
> L22: This client (namely JADExpert) provides the major JADBio functionality to python users using API calls. Requests ar

## 星数曲线

```mermaid
xychart-beta
    title "JADBio/JADBioPythonClient 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2c86e38becea` · [字段定义](../../DATASET.md)*
