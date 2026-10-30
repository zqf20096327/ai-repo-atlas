# AndreaIannoli/TOONIFY

⭐ 17 · Rust · MIT · 推送 2025-11-17 · [GitHub](https://github.com/AndreaIannoli/TOONIFY) · 个人维护

**JSON/YAML/XML/CSV 转 TOON 格式的 Rust 转换器及多语言绑定**

用 Rust 编写的通用格式转换工具：将 JSON、YAML、XML、CSV 归一化为 TOON 格式，并提供 decode_str/validate_str 解码与严格模式校验 API；CLI 支持 --token-report 输出 token 节省统计（默认 cl100k_base，可切换 o200k 面向 GPT-4o 类模型）。交付形态包括 crates.io 上的 CLI、Node.js 绑定（napi-rs）、Python 绑定（PyO3+maturin）与 Docker 镜像。构建需要 Rust 1.76+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Rust 核心库 + CLI + Node.js/Python 绑定 + Docker 镜像
- 支持 json/yaml/xml/csv/auto 嗅探输入，可配分隔符、缩进、key 折叠
- TOON→JSON 解码与严格模式校验（数组计数、缩进、路径展开冲突）
- CLI 提供 token 节省报告（cl100k_base/o200k）

## 适用场景

- 把结构化数据转成 TOON 格式以节省 LLM token
- 校验或解码已有 TOON 文档为 JSON
- 在 JS/Python 项目中集成 TOON 编解码能力

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L9: Universal converter for JSON, YAML, XML, and CSV into the TOON format with multi-language bindings.
> L74: Run `toonify --help` to view every flag. When you include `--token-report`, the CLI prints a token report using the

## 星数曲线

```mermaid
xychart-beta
    title "AndreaIannoli/TOONIFY 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `91b73a00cd84` · [字段定义](../../DATASET.md)*
