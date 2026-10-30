# noemaai-labs/noema-atlas

⭐ 16 · Rust · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/noemaai-labs/noema-atlas) · 组织维护

**本地 LLM 权重文件的 P2P 多源分发与校验网络**

面向本地大模型用户的模型权重分发工具：以内容哈希（BLAKE3/sha256）标识文件，通过签名清单声明各来源应提供的字节，下载中逐块校验后才写入缓存，同一权重跨来源去重存储。核心是 Rust 引擎，其上提供两个桌面程序（原生界面的 Atlas 与 Tauri+WebView 的 Studio）、命令行与回环网页面板；传输可走 Iroh 的 P2P 通道（QUIC/中继穿 NAT），Hugging Face 作为回退来源。支持发布签名的多源清单与本地 GGUF/Safetensors 的导入共享，默认拒绝 Pickle 与可执行文件类型。macOS/Windows/Linux 提供预构建安装包，也可用 cargo 从源码构建。

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

- 以内容哈希标识文件，签名清单校验每一字节，坏数据源当次会话被禁
- Iroh P2P 传输（BLAKE3 + QUIC，NAT 穿透），多 peer 分片并行下载，Hugging Face 作为回退
- 跨模型变体/镜像的内容去重，安装时优先 reflink/硬链接
- 两个桌面程序（Atlas 原生轻量 / Studio Tauri+WebView）共用同一引擎与存储，另有 CLI 与回环 dashboard

## 适用场景

- 从 Hugging Face 或 P2P 网络下载经校验的量化模型权重
- 在多台机器间直接点对点传输模型文件（含多分片 bundle）
- 分发已从 Hub 下架或从未发布的本地 GGUF/Safetensors 模型
- 在服务器上通过 SSH 用命令行脚本化管理模型文件

## 场景标签

 · 领域:本地 LLM 模型分发/存储

## 证据(README 行号)

> L5: Noema Atlas is a peer-to-peer network for the weight files behind local language models. A model you already hold ca
> L7: What keeps the sharing safe is that a file's identity is the digest of its own contents rather than the address it c

## 星数曲线

```mermaid
xychart-beta
    title "noemaai-labs/noema-atlas 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `61d291a404bb` · [字段定义](../../DATASET.md)*
