# Felix-au/Fragmented-Firewall

⭐ 18 · TypeScript · MIT · 推送 2026-07-29 · [GitHub](https://github.com/Felix-au/Fragmented-Firewall) · 个人维护

**有状态 AI 入侵防御系统：重组 TCP 分片并用深度学习拦截恶意载荷**

面向网关级入侵防御的防火墙系统：按五元组缓存双向流量，依 TCP 序列号重组乱序/重复/重叠/缺口的分片报文，提取序列特征后由 PyTorch 双向 LSTM 或自注意力 Transformer 模型实时判定威胁，并对恶意会话执行动态阻断与攻击 IP 临时拉黑 1 小时。提供 Scapy 实时抓包与 PCAP 回放两种模式、流量模拟器、React 运营面板及运行时模型热替换。后端 FastAPI、前端 React/Vite，支持 docker-compose 整栈部署；容器内抓包默认降级为模拟模式。实时抓包需管理员权限或 Npcap/WinPcap。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按 TCP 序列号的滑动窗口流重组，处理乱序/重叠/缺口
- PyTorch 双向 LSTM 与 Transformer 双架构实时威胁判定
- 动态黑白名单规则与攻击 IP 临时拉黑（1 小时）
- 运行时模型热替换与 docker-compose 整栈部署

## 适用场景

- 在网关处检测并阻断分片逃逸型恶意载荷
- 对 Wireshark PCAP 流量做离线威胁分析
- 在模拟环境中演练 SQL 注入/Shellcode/反弹 Shell 攻击并验证拦截效果

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L20: This system captures packet flows, buffers them per-flow, reassembles them based on TCP sequence numbers (handling 
> L41: * **State-of-State Deep Learning**: Real-time evaluation using PyTorch Bidirectional LSTM and Self-Attention Transf

## 星数曲线

```mermaid
xychart-beta
    title "Felix-au/Fragmented-Firewall 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `7530ed223ad3` · [字段定义](../../DATASET.md)*
