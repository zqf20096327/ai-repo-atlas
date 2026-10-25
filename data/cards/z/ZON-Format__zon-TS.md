# ZON-Format/zon-TS

⭐ 51 · TypeScript · MIT · 推送 2026-04-27 · [GitHub](https://github.com/ZON-Format/zon-TS) · [官网](https://zonformat.org/docs/typescript) · 个人维护

**面向 LLM 的省 token 序列化格式与 TypeScript 编解码库**

Zero Overhead Notation（ZON）是一种紧凑的数据序列化格式，以表格化编码、单字符原语（T/F、@(N) 表头）压缩 JSON 数据，README 声称相对 JSON 减少 35-70% token 且无损往返。以 npm 包 zon-format 提供，包含编码/解码、流式处理（ZonStreamEncoder/Decoder）、面向 LLM 的上下文感知编码（encodeLLM）、CLI（stats/format）与 VS Code 扩展。面向需向 LLM 传递结构化数据的开发者；基准测试覆盖 GPT-4o、Claude、Llama 3 的 tokenizer；内置文档大小/数组长度等 DOS 防护限制。格式尚在演进中（作者自述无最终定稿）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 表格化编码与单字符原语实现 JSON 数据压缩
- ZonStreamEncoder/Decoder 流式处理与 encodeLLM 上下文感知编码
- CLI（zon stats / zon format）与 VS Code 语法高亮扩展
- 内置安全限制：100MB 文档、1M 数组、100K 键、100 层嵌套

## 适用场景

- 把结构化数据编码进 LLM prompt 以减少输入 token 费用
- 在浏览器/Edge 环境（Cloudflare Workers、Vercel Edge）中编解码紧凑数据
- 用 CLI 统计与格式化 .zonf 数据文件

## 场景标签

 · 领域:LLM 基础设施/数据格式

## 证据(README 行号)

> L17: ZON is a token-efficient serialization format designed for LLM workflows. It achieves 35-50% token reduction vs JSO
> L13: **Zero Overhead Notation** - A compact, human-readable way to encode JSON for LLMs.
> L27: npm i zon-format

## 星数曲线

```mermaid
xychart-beta
    title "ZON-Format/zon-TS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-25 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `27a396696d8d` · [字段定义](../../DATASET.md)*
