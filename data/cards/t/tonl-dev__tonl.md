# tonl-dev/tonl

⭐ 833 · TypeScript · MIT · 推送 2026-08-07 · [GitHub](https://github.com/tonl-dev/tonl) · [官网](https://tonl.dev) · 组织维护

**面向 LLM token 效率的紧凑数据序列化格式与工具库**

TypeScript 实现的数据平台：定义 TONL 文本格式替代 JSON，宣称体积缩减 32-45%（字节与 token 双口径），并提供查询（JSONPath）、修改、哈希/BTree 索引、流式处理（多 GB 文件 &lt;100MB 内存）、字典/Delta/RLE 等压缩策略、TSL schema 校验与 TypeScript 类型生成。面向在提示词中嵌入结构化数据以降低 token 成本的开发者，MIT 许可，npm 安装，支持 Node.js 与浏览器（约 29.5 KB gzipped），附 CLI（encode/decode/query/validate/stats）与 VS Code 语法高亮扩展。

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

- 与 JSON 双向转换的 TONL 文本格式，含 tokenizer 感知优化
- JSONPath 查询、CRUD 修改 API 与哈希/BTree/复合索引
- 流式处理支持多 GB 文件（&lt;100MB 内存）
- TSL schema 校验（13 种约束）与 TypeScript 类型生成

## 适用场景

- 在 LLM 提示词中嵌入结构化数据以减少 token 消耗
- 用紧凑且人类可读的格式管理配置文件
- 大体积日志与数据管道的流式编码/解码
- API 响应以 text/tonl 格式传输并做 schema 校验

## 场景标签

 · 领域:数据序列化/LLM 基础设施

## 证据(README 行号)

> L5: **TONL** is a production-ready data platform that combines compact serialization with powerful query, modification, 
> L234: Reduce token costs by 32-45% when including structured data in prompts:
> L236: const prompt = `Analyze this user data:\n${doc.toTONL()}`;

## 星数曲线

```mermaid
xychart-beta
    title "tonl-dev/tonl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 832 --> 834
    line [833, 833]
```

2026-10-18 833 → 2026-10-23 833（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2e1943ebc21b` · [字段定义](../../DATASET.md)*
