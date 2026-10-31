# abrander/gguf

⭐ 14 · Go · MIT · 推送 2026-10-20 · [GitHub](https://github.com/abrander/gguf) · 个人维护

**Go 语言的 GGUF 文件读写库：解析元数据与张量字节**

提供 GGUF v1/v2/v3 文件的读取与写出（写为 v3），仅处理元数据与张量字节，不解释张量数据本身。写出时先写头部固定张量布局，支持多 goroutine 乱序写入张量，名称/类型/尺寸校验不匹配时报错；Metadata.Set 在编译期约束 Go 类型到 GGUF 类型的映射。附带 ggufmeta 命令行工具检查 GGUF 文件，gguf.Copy 可重写文件（含分片合并）并替换元数据。要求 Go 1.27 或更高版本。

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

- 读取 GGUF v1/v2/v3，写出为 v3
- 张量可乱序、多 goroutine 并发写入，头部固定布局
- gguf.Copy 重写文件/合并分片模型并替换元数据
- 附带 ggufmeta CLI 检查 GGUF 文件元数据

## 适用场景

- 在 Go 工具链中解析或修改 GGUF 模型文件的元数据
- 将分片 GGUF 模型合并为单文件并重写元数据
- 查看 GGUF 模型文件的张量结构与元数据信息

## 场景标签

 · 领域:LLM 基础设施/模型文件格式

## 证据(README 行号)

> L5: This is a Go package for reading and writing GGUF files.
> L7: The package is only concerned with the metadata and the tensor bytes. It does

## 星数曲线

```mermaid
xychart-beta
    title "abrander/gguf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `9ecc047f43ab` · [字段定义](../../DATASET.md)*
