# weaviate/weaviate-go-client

⭐ 61 · Go · BSD-3-Clause · 推送 2026-10-25 · [GitHub](https://github.com/weaviate/weaviate-go-client) · 组织维护

**Weaviate 数据库的官方 Go 客户端库**

Weaviate 向量数据库的原生 Go 客户端，供开发者在 Go 程序中连接 Weaviate 实例（如 localhost:8080）、获取实例元信息并进行数据操作。通过 go get 安装 v5 版本并在 go.mod 中声明依赖；README 标注 v5.0.0 因 go.mod 文件格式错误无法安装，建议使用 v5.0.1 及以上版本。仓库由 weaviate 组织维护，附文档链接与构建状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Weaviate 的原生 Go 客户端
- 通过 go get 安装，go.mod 声明依赖
- README 明确提示 v5.0.0 版本不可安装，需 v5.0.1+

## 适用场景

- 在 Go 项目中接入 Weaviate 向量数据库
- 连接本地或远程 Weaviate 实例并获取元信息

## 场景标签

`向量数据库` · 领域:知识与检索

## 证据(README 行号)

> L3: A native Go client for Weaviate.
> L7: > :warning: `v5.0.0` cannot be installed due to a malformed `go.mod` file.

## 星数曲线

```mermaid
xychart-beta
    title "weaviate/weaviate-go-client 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-26 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d9056238b1e5` · [字段定义](../../DATASET.md)*
